
import runpod

from gpu_app import ResumeRequest, predict


def handler(job):
    data = job.get("input", {})
    text = data.get("text", "")

    if not isinstance(text, str) or not text.strip():
        return {"error": "Resume text is required"}

    result = predict(ResumeRequest(text=text))

    return result


runpod.serverless.start({"handler": handler})
