function GET_COMP(name){
    for (var i = 1; i <= app.project.numItems; i++) {
        var item= app.project.items[i];
        if (item instanceof CompItem && item.name == name) {
              return item;
        }
    }
}
var wGLhtYAmfTY = app.project.items.addComp('hello', 1280, 720, 1.78, 30.0, 30.0);var ggkMWvgvEok = wGLhtYAmfTY.layers.addSolid([0.0, , 100,100,1);ggkMWvgvEok.position.setValue([3, 4, 3]);ggkMWvgvEok.name = 'sir';ggkMWvgvEok.width = 1280ggkMWvgvEok.height = 720