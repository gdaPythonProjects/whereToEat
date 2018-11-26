  
    var wyniki = {{przeslij_html|tojson}};
    iloscWynikow=(wyniki.length/4);
    console.log(wyniki);
    console.log("ilość wyników: " + iloscWynikow);
    function loadMapScenario() {
     var map = new Microsoft.Maps.Map(document.getElementById('myMap'), {});
    while (iloscWynikow>0){
        var votes =wyniki[3]
         var menuurl=wyniki[4];
        if(votes==0){votes=""};
        map.entities.push(new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(wyniki[0],wyniki[1]), {title: wyniki[2], text:votes}));
       var z = 5;
        while(z>0){
            wyniki.shift();
            z--;
            }

            
        iloscWynikow--;
    }}