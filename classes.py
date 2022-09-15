import stl
from mpl_toolkits import mplot3d
from matplotlib import pyplot


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
        self.figure = None
        self.axes = None
        self.scale = None

    def get_volume(self):
        self.volume, _, inertia = self.mesh.get_mass_properties()
        return self.volume

    def get_dimensions(self):
        self.dim_x = self.mesh.x.max() - self.mesh.x.min()
        self.dim_y = self.mesh.y.max() - self.mesh.y.min()
        self.dim_z = self.mesh.z.max() - self.mesh.z.min()
        return [self.dim_x, self.dim_y, self.dim_z]

    def show_object(self):
        # Create a new plot
        self.figure = pyplot.figure()
        self.axes = mplot3d.Axes3D(self.figure)

        # Vectors to plot
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(self.mesh.vectors))

        # Auto-scale to the mesh size
        self.scale = self.mesh.points.flatten()
        self.axes.auto_scale_xyz(self.scale, self.scale, self.scale)

        # Show the plot to the screen
        # pyplot.show()


class Prize:
    def __init__(self, volume, dimensions):
        self.finalprize = None
        self.material_f = None
        self.quality_f = None
        self.material = None
        self.thickness = None
        self.realvol = None
        self.materials = None
        self.volume = volume
        self.dimensions = dimensions
        self.infill = None

    def possibility(self):
        print('Można drukować z:')
        if self.dimensions[0] < 200 and self.dimensions[1] < 200 and self.dimensions[2] < 200:
            self.materials = ['PLA', 'PETG', 'ASA', 'ABS', 'TPU']
            print(self.materials)
        elif self.dimensions[0] < 400 and self.dimensions[1] < 400 and self.dimensions[2] < 400:
            self.materials = ['PLA', 'PETG']
            print(self.materials)
        else:
            print('Uwaga wydruk wielkoformatowy - prosimy o kontakt.')
        return self.materials

    def realvolume(self, infill):
        self.infill = infill
        self.realvol = self.volume * (0.2 + 0.8 * self.infill)
        return self.realvol

    def choose_quality(self, thickness):
        self.thickness = thickness
        if self.thickness == 0.28:
            self.quality_f = 0.8
            return self.quality_f
        elif self.thickness == 0.2:
            self.quality_f = 1
            return self.quality_f
        elif self.thickness == 0.16:
            self.quality_f = 1.25
            return self.quality_f
        elif self.thickness == 0.12:
            self.quality_f = 1.5
            return self.quality_f
        else:
            print('zla wartość')
            return None

    def choose_material(self, material):
        self.material = material
        if self.material == 'PLA':
            self.material_f = 1
            return self.material_f
        elif self.material == 'PETG':
            self.material_f = 1.25
            return self.material_f
        elif self.material == 'ASA':
            self.material_f = 1.5
            return self.material_f
        elif self.material == 'ABS':
            self.material_f = 1.75
            return self.material_f
        elif self.material == 'TPU':
            self.material_f = 2
            return self.material_f
        else:
            print('zly material')
            return None

    def final_prize_calc(self):
        self.finalprize = 10 + (self.realvol / 1000 * self.quality_f * self.material_f)
        return self.finalprize

