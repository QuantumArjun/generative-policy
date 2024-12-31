import sys
sys.path.append(".")
from config import Config
import json
from flask import Flask, jsonify, render_template, request
from agents.human_elicitation.base import BaseHumanElicitation
import os


model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")

human_elicitation = BaseHumanElicitation(model_config, domain="gun laws")
app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/get_next_prompt", methods=["POST"])
def get_next_prompt():
  prolific_id = request.form.get("prolific_id")
  prompt = human_elicitation.question_human()

  return jsonify({
      "prompt": prompt,
      "evaluation_prompt": "evaluation prompt",
      "test_samples": "test samples",
      "mode": "chat",
  })


@app.route("/update", methods=["POST"])
def update():
  """
  Sends user message (if exists) and queries active learning agent for next query
  """
  user_message = request.form.get("user_message")
  prolific_id = request.form.get("prolific_id")
  human_elicitation.update_human_response(user_message)
  return jsonify({"response": prolific_id})


@app.route("/save", methods=["POST"])
def save():
  prolific_id = request.form.get("prolific_id")
  with open(os.path.join(SAVE_DIR, f"{prolific_id}.json"), "w") as f:
    json.dump(prolific_id_to_user_responses[prolific_id], f, indent=2)
  return jsonify({"response": "done"})


@app.route("/submit_evaluation", methods=["POST"])
def evaluation_submission():
  prolific_id = request.form.get("prolific_id")
  user_labels = []
  for idx, test_sample in enumerate(prolific_id_to_experiment_type[prolific_id]["prompt"]["test_samples"]):
    user_labels.append({
        "sample": test_sample,
        "label": request.form.get(f"test-case-{idx}"),
        "explanation": request.form.get(f"test-case-{idx}-explanation"),
    })
  prolific_id_to_user_responses[prolific_id]["evaluation_results"] = user_labels
  save()
  return jsonify({"response": "done"})


@app.route("/submit_feedback", methods=["POST"])
def feedback_submission():
  prolific_id = request.form.get("prolific_id")
  for feedback_type in request.form:
    if feedback_type.startswith("feedback_"):
      prolific_id_to_user_responses[prolific_id]["feedback"][feedback_type] = request.form.get(
        feedback_type)
  save()
  return jsonify({"response": "done"})


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8000)
