# Import potrzebnych bibliotek
import open3d as o3d
import numpy as np
import laspy

#Wczytanie chmury punktów w formacie las
def wczytanie_chmury_punktow_las_konwersja_do_o3d(plik):
    las_pcd = laspy.read(plik)
    x = las_pcd.x
    y = las_pcd.y
    z = las_pcd.z

    #Normalizacja koloru
    r = las_pcd.red/max(las_pcd.red)
    g = las_pcd.green/max(las_pcd.green)
    b = las_pcd.blue/max(las_pcd.blue)
    
    #Konwersja do formatu NumPy do o3d
    #Stackuje na sobie tablice z x,y,z - klade x na y, y na z - i transpoza
    las_points = np.vstack((x,y,z)).transpose()
    las_colors = np.vstack((r,g,b)).transpose()
    chmura_punktow = o3d.geometry.PointCloud()
    chmura_punktow.points = o3d.utility.Vector3dVector(las_points)
    chmura_punktow.colors = o3d.utility.Vector3dVector(las_colors)
    
    return chmura_punktow