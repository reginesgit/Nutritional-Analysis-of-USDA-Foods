var tbody = d3.select("tbody");

d3.json('/').then(function(data){
    console.log(data);
    console.log(data[0].foods[0].foodNutrients[0].nutrientName)

    var foods = data[0].foods

    foods.forEach(function(food) {
        console.log(food);
        var row = tbody.append("tr");
        row.append("td").html(`<a href="/foodNutrients/${food.fdcId}">${food.brandOwner}</a>`);
        row.append("td").text(food.ingredients);
    });


    // Part 1
    var trace1 = {
        x: ["beer", "wine", "martini", "margarita",
        "ice tea", "rum & coke", "mai tai", "gin & tonic"],
        y: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
        type: "bar"
    };
    
    var data = [trace1];
    
    var layout = {
        title: "'Bar' Chart"
    };
    
    Plotly.newPlot("plot", data, layout);
    


}).catch(function(error){
    console.log(error);
});