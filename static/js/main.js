document.getElementById("generate-meal-plan").addEventListener("click", async () => {
    // Get input values
    const proteinMin = document.getElementById("proteinMin").value;
    const proteinMax = document.getElementById("proteinMax").value;
    const carbsMin = document.getElementById("carbsMin").value;
    const carbsMax = document.getElementById("carbsMax").value;
    const energyMin = document.getElementById("energyMin").value;
    const energyMax = document.getElementById("energyMax").value;

    const inputData = {
        proteinMin: parseInt(proteinMin),
        proteinMax: parseInt(proteinMax),
        carbsMin: parseInt(carbsMin),
        carbsMax: parseInt(carbsMax),
        energyMin: parseInt(energyMin),
        energyMax: parseInt(energyMax),
    };

    try {
        // Send data to backend
        const response = await fetch("/generate-meal-plan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(inputData)
        });

        const mealPlan = await response.json();
        localStorage.setItem("mealPlan", JSON.stringify(mealPlan));
        window.location.href = "/output";
    } catch (error) {
        console.error("Error generating meal plan:", error);
        alert("An error occurred while generating the meal plan. Please try again.");
    }
});
