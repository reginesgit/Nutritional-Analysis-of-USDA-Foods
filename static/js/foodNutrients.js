d3.json('/').then(function(data){
    console.log(data);
    console.log(data[0].foods[0].foodNutrients[0].nutrientName)
    console.log(fdcId)
    var food = data[0].foods
        .filter(food => food.fdcId == fdcId)  //Filter to the food that was clicked.
    console.log(food)
    var foodNutrients = food[0].foodNutrients
        .filter(foodNutrient => {
            console.log(foodNutrient)
            if(foodNutrient.unitName === "MG" || foodNutrient.unitName === "G"){
                return true
            }
        })
        .map(foodNutrient => { // Create an array of food nutrients Name and Number.
            var nutrientNumber = parseInt(foodNutrient.nutrientNumber);
            if(foodNutrient.unitName == "MG"){
                nutrientNumber = nutrientNumber/1000
            }
            return {
                nutrientName: foodNutrient.nutrientName,
                nutrientNumber: nutrientNumber,
                unitName: foodNutrient.unitName
            }
        })

    console.log(foodNutrients)

    var xNutrients = foodNutrients
        .filter(foodNutrient => foodNutrient.unitName === "G")
        .map(foodNutrient => foodNutrient.nutrientName)
    var yNutrients = foodNutrients
        .filter(foodNutrient => foodNutrient.unitName === "G")
        .map(foodNutrient => foodNutrient.nutrientNumber)


    console.log(xNutrients)
    console.log(yNutrients)

    // Part 1
    var traceBar = {
        x: xNutrients,
        y: yNutrients,
        type: "bar"
    };
    
    var dataBar = [traceBar];
    
    var layoutBar = {
        title: "Nutrients Chart"
    };
    
    Plotly.newPlot("plot", dataBar, layoutBar);
    
    // Plot 2

    var xVitamins = foodNutrients
    .filter(foodNutrient => foodNutrient.unitName === "MG")
    .map(foodNutrient => foodNutrient.nutrientName)
    var yVitamins = foodNutrients
    .filter(foodNutrient => foodNutrient.unitName === "MG")
    .map(foodNutrient => foodNutrient.nutrientNumber)

    var tracePie = {
        labels: xVitamins,
        values: yVitamins,
        type: "pie"
    };
    
    var dataPie = [tracePie];
    
    var layoutPie = {
        title: "Vitamins Chart"
    };
    
    Plotly.newPlot("plotPie", dataPie, layoutPie);


}).catch(function(error){
    console.log(error);
});