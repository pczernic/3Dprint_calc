from classes import StlObject, MeshObject, Prize


if __name__ == '__main__':
    model = StlObject('10mmx3.stl')
    mesh = MeshObject(model.stl2mesh())
    vol = mesh.get_volume()
    dims = mesh.get_dimensions()
    print('volume: {}'.format(vol))
    print('dimensions: {}'.format(dims))
    mesh.show_object()

    calc = Prize(vol, dims)
    calc.possibility()
    realvol = calc.realvolume(1)
    quality = calc.choose_quality(0.12)
    material = calc.choose_material('PLA')
    final_prize = calc.final_prize_calc()
    print(final_prize)





