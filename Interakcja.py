# Import potrzebnych bibliotek
import open3d as o3d
import numpy as np

def manualne_przycinanie_chmury_punktow(chmura_punktow):
    #Instrukcja w readme.txt
    o3d.visualization.\
        draw_geometries_with_editing(   [chmura_punktow],\
                                         window_name="Przycinanie chmury punktów",\
                                         left=5, top=30)
            
def pomiar_punktow_na_chmurze(chmura_punktow):
    #Instrukcja w readme.txt
    vis = o3d.visualization.VisualizerWithEditing()
    
    vis.create_window(window_name="Pomiar punktów")
    vis.add_geometry(chmura_punktow)
    vis.run()                   #user picks points
    vis.destroy_window()        #user closes window by clicking q
    
    
    print("Koniec pomiaru")
    print(vis.get_picked_points())
    
    pts = vis.get_picked_points()
    pts_coordinates = np.array(o3d.utility.Vector3dVector(chmura_punktow.select_by_index(pts, invert = False).points))
    
    # return vis.get_picked_points(), pts_coordinates
    return vis.get_picked_points()

def obliczanie_obszaru_opracowania(chmura_punktow, typ = 'AxisAlignedBoundingBox'):
    if typ == 'AxisAlignedBoundingBox':
        print("Obliczanie obszaru opracowania zorientowanego względem osi XYZ")
        aabb = chmura_punktow.get_axis_aligned_bounding_box()
        aabb.color = (1, 0, 0)
        print(aabb)
        o3d.visualization.draw_geometries([chmura_punktow,aabb],window_name='AxisAlignedBoundingBox', left=5, top=30)
    else:
        print("Obliczanie obszaru opracowania zorientowanego względem chmury punktów")
        obb = chmura_punktow.get_oriented_bounding_box()
        obb.color = (0, 1, 0)
        print(obb)
        o3d.visualization.draw_geometries([chmura_punktow,obb], window_name = 'OrientedBoundingBox', left=5, top=30)