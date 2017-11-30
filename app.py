layer = iface.activeLayer();

Fs = layer.getFeatures();

U = [Fs.getFeatures.next()];

for f in Fs: U.append(f);

start = QgsPoint(x,y);

end = QgsPoint(x,y);

v_layer = QgsVectorLayer("LineString", "line", "memory")

pr = v_layer.dataProvider();

pr.addFeatures([seg]);

v_layer.updateExtents();

QgsMapLayerRegistry.instance().addMapLayers([v_layer]);