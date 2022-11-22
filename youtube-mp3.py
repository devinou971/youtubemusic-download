from pytube import YouTube
from os import listdir
from os.path import isfile, join, isdir
import pandas as pd

#Chemin du dossier qui contient les sous-dossiers
path="C:/Users/emmao/OneDrive/Documents/Musiques/"

#Les sous-dossiers (pour trier mes musiques)
dossiers = [d for d in listdir(path) if isdir(join(path,d))]

#Les musiques
fichiers=[]
for d in dossiers:
    path_d = path+d
    fichiers = fichiers + [f for f in listdir(path_d) if isfile(join(path_d, f))]

fichiers_upper = [x.upper() for x in fichiers]

error = 0
good = 0
for d in dossiers:
    excel_data = pd.read_excel('C:/Users/emmao/OneDrive/Documents/Dev/many-youtube-mp3/Liste_musiques.xlsx', d)
    data = pd.DataFrame(excel_data, columns=['URL', 'Nom', 'Erreur'])

    init_len = len(data)

    for i in range(0,init_len):
        url = data.loc[i][0]
        name = data.loc[i][1]+".mp3"
        

        try:
            yt_object = YouTube(data.loc[i][0])
        except:
            data.loc[[i],["Erreur"]] = "URL invalide"
            error = error+1
        else:
            if name.upper() not in fichiers_upper:
                audio = yt_object.streams.filter(only_audio = True).first()
                audio.download(output_path=path+d,filename=name)
                
                data.loc[[i],["Erreur"]] = "OK"
                fichiers_upper.append(name.upper())
                print(name + " téléchargée dans " + d)
                good = good+1
            else:
                data.loc[[i],["Erreur"]] = "Musique déjà téléchargée"
                print("ERREUR : problème avec " + name + " dans " + d)
                error = error+1


    data.drop( data[ data['Erreur'] == "OK" ].index, inplace=True)
    with pd.ExcelWriter('Liste_musiques.xlsx',mode='a', if_sheet_exists="replace") as writer:  
        data.to_excel(writer, sheet_name=d)

print("Nombre de musiques téléchargées : " + str(good))
print("Nombre de musiques non téléchargées : " + str(error))
