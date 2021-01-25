function GET_COMP(name){
    for (var i = 1; i <= app.project.numItems; i++) {
        var item= app.project.items[i];
        if (item instanceof CompItem && item.name == name) {
              return item;
        }
    }
}
