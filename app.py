from flask import Flask, render_template, request, jsonify

from pipeline import research_pipeline


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/research", methods=["POST"])
def research():
    data = request.get_json()

    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({
            "error": "Please enter a research topic."
        }), 400

    try:
        result = research_pipeline.invoke({
            "topic": topic
        })

        return jsonify({
            "topic": topic,
            "report": result.get("report", ""),
            "critique": result.get("critique", "")
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)