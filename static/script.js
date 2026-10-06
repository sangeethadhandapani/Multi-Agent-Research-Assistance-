async function startResearch() {

    const topicInput = document.getElementById("topic");
    const button = document.getElementById("researchButton");
    const loading = document.getElementById("loading");
    const resultSection = document.getElementById("resultSection");

    const topic = topicInput.value.trim();

    if (!topic) {
        alert("Please enter a research topic.");
        return;
    }

    // Disable button while research is running
    button.disabled = true;
    button.textContent = "Researching...";

    // Show loading message
    loading.classList.remove("hidden");

    // Hide previous results
    resultSection.classList.add("hidden");

    try {

        const response = await fetch("/research", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                topic: topic
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Research failed.");
        }

        // Display topic
        document.getElementById("resultTopic").textContent =
            "Topic: " + data.topic;

        // Display report
        document.getElementById("report").textContent =
            data.report;

        // Display critic review
        document.getElementById("critique").textContent =
            data.critique;

        // Show results
        resultSection.classList.remove("hidden");

    } catch (error) {

        alert("Error: " + error.message);

    } finally {

        // Hide loading
        loading.classList.add("hidden");

        // Enable button again
        button.disabled = false;
        button.textContent = "Research";
    }
}