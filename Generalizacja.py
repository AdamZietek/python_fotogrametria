import open3d as o3d

#Downsampling chmur punktów
def regularyzacja_chmur_punktow(chmura_punktow, odleglosc_pomiedzy_wokselami):
    chmura_punktow_woksele = chmura_punktow.\
        voxel_down_sample(voxel_size=odleglosc_pomiedzy_wokselami)
    print("Wyswietlanie chmury punktow w regularnej siatce wokseli\
           odleglosc %f: " %odleglosc_pomiedzy_wokselami)
    o3d.visualization.draw_geometries([chmura_punktow_woksele], left=5, top=30)
    return chmura_punktow_woksele

def usuwanie_co_n_tego_punktu_z_chmury_punktow(chmura_punktow, co_n_ty_punkt):
    chmura_punktow_co_n_ty = chmura_punktow.\
        uniform_down_sample(every_k_points=co_n_ty_punkt)
    print("Wyświetlanie chmura punktów zredukowanej co %i: " % co_n_ty_punkt)
    o3d.visualization.draw_geometries([chmura_punktow_co_n_ty], left=5, top=30)
    return chmura_punktow_co_n_ty