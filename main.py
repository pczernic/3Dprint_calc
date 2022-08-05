from classes import StlObject, MeshObject


if __name__ == '__main__':
    model = StlObject('playing_card_holder.stl')
    mesh = MeshObject(model.stl2mesh())
    vol = mesh.get_volume()
    dims = mesh.get_dimensions()
    print(vol)
    print(dims)
    mesh.show_object()



