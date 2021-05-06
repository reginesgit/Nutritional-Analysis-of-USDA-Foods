var tbody = d3.select("tbody");

d3.json('/home_data').then(function(data){
    console.log(data);
    console.log(data[0].foods[0].foodNutrients[0].nutrientName)

    var foods = data[0].foods

    foods.forEach(function(food) {
        console.log(food);
        var row = tbody.append("tr");
        row.append("td").html(`<a href="/foodNutrients/${food.fdcId}">${food.brandOwner}</a>`);
        row.append("td").text(food.ingredients);
    });

}).catch(function(error){
    console.log(error);
});