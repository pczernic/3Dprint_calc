import stl


class StlObject:
    def __init__(self, path):
        self.volume = None
        self.mesh = None
        try:
            if not path.endswith('.stl'):
                print('Wrong file extension! This program supports only .stl files!')
        except AttributeError:
            print('Wrong path!')
        self.stl_file = path

    def stl2mesh(self):
        self.mesh = stl.mesh.Mesh.from_file(self.stl_file)
        return self.mesh


class MeshObject:
    def __init__(self, mesh):
        self.mesh = mesh
        self.dim_x = 0
        self.dim_y = 0
        self.dim_z = 0
        self.volume = 0

    def get_volume(self):
        self.volume, _, inertia = self.mesh.get_mass_properties()
        return self.volume

    def get_dimensions(self):
        self.dim_x = self.mesh.x.max() - self.mesh.x.min()
        self.dim_y = self.mesh.y.max() - self.mesh.y.min()
        self.dim_z = self.mesh.z.max() - self.mesh.z.min()
        return [self.dim_x, self.dim_y, self.dim_z]
