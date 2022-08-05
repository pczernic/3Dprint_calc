import stl
from stl import mesh
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

        # Auto scale to the mesh size
        self.scale = self.mesh.points.flatten()
        self.axes.auto_scale_xyz(self.scale, self.scale, self.scale)

        # Show the plot to the screen
        pyplot.show()