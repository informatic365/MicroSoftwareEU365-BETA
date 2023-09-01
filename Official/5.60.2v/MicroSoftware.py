from ttkbootstrap import *
from customtkinter import *
from ttkbootstrap.dialogs import Messagebox
from pytube import YouTube
import os
import sys
import subprocess
import ctypes
import configparser
import threading as th
import time as tm
from datetime import *
from tkinter import filedialog, messagebox
import random
import string
import psutil
import eel
import concurrent.futures
import requests
from firebase_admin import credentials, firestore
import firebase_admin
import winsound
import webbrowser
import socket

path = os.path.dirname(os.path.realpath(__file__))
PATH = path
BOLD = "bold"
sys.getsizeof(path)
english = "English"
italiano = "Italiano"
spanish = "Español"

if __name__ == "__main__":
    apiKey = "apiKey"
    authDomain = "authDomain"
    databaseURL = "databaseURL"
    projectId = "projectId"
    storageBucket = "storageBucket"
    messagingSenderId = "messagingSenderId"
    appId = "appId"
    measurementId = "measurementId"
    __credentials__ = {
        apiKey: "AIzaSyCWqQwOw86lFxVMLlCuHmLNPcQX7R7nHg0",
        authDomain: "windb-core.firebaseapp.com",
        databaseURL: "https://windb-core-default-rtdb.firebaseio.com",
        projectId: "windb-core",
        storageBucket: "windb-core.appspot.com",
        messagingSenderId: "1068572480216",
        appId: "1:1068572480216:web:55d0aa6553e3c02ee63dad",
        measurementId: "G-2SGBDNVZNK"
    }
    __config__ = {
        "type": "service_account",
        "project_id": "windb-core",
        "private_key_id": "e9b97a3b0dae9c25e58d0173deeb2fa89b710e92",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDxXXL+VrfxAK/s\n+T9+S3egR8Mg6p6q5BwMQm9wPchcANkQFtzxIXjj6Lf2fr7vEDkYWKdj3HaSr93z\npCQxTeBh6gnG65nCf6yIoBR9r2KgOqFqf7QXgGi7PHjfIJ8fZNdfiBZ6x1JPSW1W\nYbhi6AFml1fyD7K31wXL6xzutIN/pd1pBo10FE3TKxr6q6r+nkNVHChyGl1NfSKS\n+srS9nRiNj+P8iIQQFziao4PdIA6p8Hp4RxvtR1RuAKFqIJ7vPotbUS62EqZver4\n5nj47RmvAbNXNG+5c5zylQuUBoFoqAS0ovc4hV1WvZCj5ZvMaYLqz/2R2WRw5mVq\nEm0TnLw5AgMBAAECggEAAKbtBw3GBVc0/BBBt4Fg/OecueOWxj7qA+JDdoHp0k41\nR+myTJt3l5c66GYeW9TgvQJZgQSCmuUk1bVRXLaJZX8fA72b5q526wKSgGY48omR\nNisX2gIzv9SLJHOSqOBnA/M0UYrlNWFTjVdwirt2ORthD/5/XNquZ+CsrUkDDu7E\nlhidFtQpwOFxV+mUNg4sJog5sH4fKPpjAOXZpjq9b0poDmVddkLLOrq9aGMNKPrh\nFYYPMRMPBKuuRRvF6WZH0rFT8FVU8N8bQK1B0aybG8vFB81uUj11PRWDsKkv/uxF\niNyZ1oenKfBnNAEZMXKqO5LRWAZVfrCd6jtvPE7l5QKBgQD+IoFZ8C3trn6EmrQH\n16Oa/h9q2Fejn5Nnq82rALcWatKwOGPnuIfjQTU7vdq0LUUw8SORud68cBWZASxn\n0Kh7FKgkOscA9bgzHkK6QoLRV4cpbq8WEww9FO6j2cZl6wSVooOENbivmB1HA/qy\ndmSGki63kGHpuaynhYb2N7JfBQKBgQDzIvNmyLjtWKkVGitd/Nqxu0vyIj1DVMbW\neFdZZfawaWmQo8wHjaUdISTtyeNTj9KISrvI1gIzSuYYRb3vw5l9CfKzPq6kFAM5\npkiDdPOGcPVUz6JzgGf70dyFHYuTICJya6VqAG1B0XiJPACanGyKpC24LAJCXNaw\ncnZmh9vmpQKBgFscc9OS0GSOUr2n2TOWlAlVYl4kAgefhnF8ntfYAcv/sFmNXgQN\nnGpVToiEoIxITq4lReNRCBH2/UdFrG3r2PuHhGC40e/+KHPrPXEZt1zmTIcGL69y\nVMjxYD1OLlsLzzD2esBDolsR5i03uAGTgKbecfFNykzJTKUisihD/6chAoGBAK9d\nJRucaK1gBkwfHOpkZsRMaAGTqoY2zleAYtgrD9u7nBVj3tQP2OiCsGUF+X2avWnq\nJTk9Ckc+nWkiXFVjygACvdeEvWfAu3bINYMDRmZQcNKkE/Kkyds6SYiFf9c1FUNb\n2unyttsDH6Iz8eeSLUNuGT++Fj8RQRPw6u8WzIe1AoGBAO/ChWSCSOykUBAG5K+7\nUgPXq6qd115S00BsoUpxNwogBdFL+f6izf0EbBBi5lbtHz0ZbLHP9kv/0PPr9kxX\nLbX5PR/PW9Vu9iJFSVsgvNdjqnz/IgKiplTBIP+mSaDSaK94zV2go0qwJvDduFvB\nQBouFoY2g/AyLxHZibTvlJx8\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-305ea@windb-core.iam.gserviceaccount.com",
        "client_id": "102399514324291509641",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-305ea%40windb-core.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
    dll_core = credentials.Certificate(__config__)
    firebase_admin.initialize_app(dll_core, __credentials__)
    db = firestore.client()
    class exit_configure():
        def __init__(self) -> None:
            try:
                console = configparser.ConfigParser()
                console.read(f"{path}/system/settings.ini")
                get_lang = console.get("MicroSoftware", "language-set")
                if get_lang == "English":
                    msg = "Are you sure you quit MicroSoftware?"
                elif get_lang == "Italiano":
                    msg = "Sei sicuro di uscire da MicroSoftware?"
                elif get_lang == "Spanish":
                    msg = "¿Estás seguro de que saliste de MicroSoftware?"
                else:
                    msg = "Are you sure you quit MicroSoftware?"
                if boolean("MicroSoftware", "enable-closing-message"):
                    if messagebox.askyesno(message=msg, title="Warning!"):
                        sys.exit()
                    else:
                        pass
                else:
                    sys.exit()
            except Exception:
                sys.exit()
    def checking():
        root.unbind("<F1>")
        root.after_cancel(set_start_timer)
        go()
    class go():
        def __init__(self) -> None:
            class home():
                def __init__(self, username) -> None:
                    class adv():
                        def __init__(self) -> None:
                            pass
                    class view_information():
                        def __init__(self) -> None:
                            def conf():
                                root.focus_set()
                                info.destroy()
                            info = Toplevel(title="Information")
                            info.grab_set()
                            info.update()
                            info.focus_set()
                            info.iconbitmap(f"{PATH}/system/src/icon.ico")
                            iwidth = 400
                            iheight = 300
                            ix = (info.winfo_screenwidth() // 2 - iwidth // 2)
                            iy = (info.winfo_screenheight() // 2 - iheight // 2)
                            info.geometry(f"{iwidth}x{iheight}+{ix}+{iy}")
                            info.focus_set()
                            info.resizable(False, False)

                            label = Label(info, text="Information", font=("Roboto", 25, BOLD))
                            label.pack(padx=5, pady=5, anchor="nw")
                            text_box_information = Text(info, borderwidth=0)
                            text_box_information.pack()



                            info.protocol("WM_DELETE_WINDOW", conf)
                            info.mainloop()
                    class settings():
                        def __init__(self) -> None:
                            def set_ecm(*args):
                                if ecmvar.get() == "True":
                                    settings_loader.set("MicroSoftware", "enable-closing-message", "True")
                                    with open(f"{PATH}/system/settings.ini", "w") as set_ecm0:
                                        settings_loader.write(set_ecm0)
                                elif ecmvar.get() == "False":
                                    settings_loader.set("MicroSoftware", "enable-closing-message", "False")
                                    with open(f"{PATH}/system/settings.ini", "w") as set_ecm1:
                                        settings_loader.write(set_ecm1)
                            class set_saves():
                                def __init__(self, *args) -> None:
                                    if splvar.get() == "True":
                                        settings_loader.set("MicroSoftware", "enable-splash-screen", "True")
                                        with open(f"{path}/system/settings.ini", "w") as set_ess0:
                                            settings_loader.write(set_ess0)
                                    elif splvar.get() == "False":
                                        settings_loader.set("MicroSoftware", "enable-splash-screen", "False")
                                        with open(f"{path}/system/settings.ini", "w") as set_ess1:
                                            settings_loader.write(set_ess1)
                                    
                            class set_settings_lang_for_user():
                                def __init__(self, *args) -> None:
                                    get = lsvar.get()
                                    if get == "English":
                                        core_frame.config(text="Settings")
                                        title_class_1_winset.config(text="MicroSoftware Settings")
                                        core_frame_class_2.config(text="Advanced")
                                        ctx.configure(text="Enable splash screen")
                                        ctx_1.configure(text="Enable closing message")
                                    elif get == "Italiano":
                                        core_frame.config(text="Impostazioni")
                                        title_class_1_winset.config(text="Impostazioni di MicroSoftware")
                                        core_frame_class_2.config(text="Avanzate")
                                        ctx.configure(text="Abilita il splash screen")
                                        ctx_1.configure(text="Abilita messaggio di chiusura")
                                    elif get == "Español":
                                        core_frame.config(text="Ajustes")
                                        title_class_1_winset.config(text="Ajustes de MicroSoftware")
                                        core_frame_class_2.config(text="Avanzada")
                                        ctx_1.configure(text="Habilitar mensaje de cierre")
                            def conf():
                                winset.destroy()
                                root.focus_set()
                            winset = Toplevel(title="MicroSoftware Enterprise 5.60.2v - Settings")
                            winset.grab_set()
                            winset.focus_set()
                            winset.deiconify()
                            winset.iconbitmap(f"{PATH}/system/src/settings_image.ico")
                            winset.focus_set()
                            winset.resizable(False, False)
                            swidth = 1310
                            sheight = 720
                            sx = (winset.winfo_screenwidth() // 2 - swidth // 2)
                            sy = (winset.winfo_screenheight() // 2 - sheight // 2)
                            winset.geometry(f"{swidth}x{sheight}+{sx}+{sy}")
                            winset.protocol("WM_DELETE_WINDOW", conf)

                            settings_loader = configparser.ConfigParser()
                            settings_loader.read(f"{PATH}/system/settings.ini")
                            getbool = settings_loader.getboolean
                            get_str_int = settings_loader.get
                            splvar = StringVar()
                            stvar = StringVar()
                            ecmvar = StringVar()
                            lsvar = StringVar()
                            uvar = StringVar()
                            cipvar = StringVar()
                            uisvar = StringVar()
                            # Splash screen
                            if getbool("MicroSoftware", "enable-splash-screen"):
                                splvar.set("True")
                            else:
                                splvar.set("False")
                            # Set Trasparency
                            if get_str_int("MicroSoftware", "set-trasparency") == "1":
                                stvar.set("1")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.9":
                                stvar.set("0.9")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.8":
                                stvar.set("0.8")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.7":
                                stvar.set("0.7")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.6":
                                stvar.set("0.6")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.5":
                                stvar.set("0.5")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.4":
                                stvar.set("0.4")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.3":
                                stvar.set("0.3")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.2":
                                stvar.set("0.2")
                            elif get_str_int("MicroSoftware", "set-trasparency") == "0.1":
                                stvar.set("0.1")
                            else:
                                stvar.set("1")
                            # Enable closing messagebox
                            if getbool("MicroSoftware", "enable-closing-message"):
                                ecmvar.set("True")
                            else:
                                ecmvar.set("False")
                            # Language set
                            if get_str_int("MicroSoftware", "language-set") == "English":
                                lsvar.set("English")
                            elif get_str_int("MicroSoftware", "language-set") == "Italiano":
                                lsvar.set("Italiano")
                            elif get_str_int("MicroSoftware", "language-set") == "Spanish":
                                lsvar.set("Español")
                            else:
                                lsvar.set("English")
                            # username
                            get_username = get_str_int("MicroSoftware", "username")
                            
                            # Design
                            BOLD = "bold"
                            winstyle = Style()
                            
                            core_frame = Labelframe(winset, text="")
                            core_frame.pack(padx=100, pady=75, fill=BOTH, expand=True)
                            title_class_1_winset = Label(core_frame, text="", font=("Helvetica", 25, BOLD))
                            title_class_1_winset.pack(anchor="nw", pady=10, padx=10)
                            ct_core_frame = Frame(core_frame)
                            ct_core_frame.place(relx=0.5, rely=0.55, anchor=CENTER)
                            core_frame_class_1 = Labelframe(ct_core_frame, text="Default", width=400, height=450)
                            core_frame_class_1.pack(side=LEFT, padx=10)
                            core_frame_class_2 = Labelframe(ct_core_frame, text="", width=400, height=450)
                            core_frame_class_2.pack(side=RIGHT, padx=10)
                            ctx = CTkSwitch(core_frame_class_1, variable=splvar, onvalue="True", offvalue="False", command=set_saves, text="")
                            ctx.place(relx=0.1, rely=0.1)
                            ctx_1 = CTkSwitch(core_frame_class_1, text="", variable=ecmvar, onvalue="True", offvalue="False", command=set_ecm)
                            ctx_1.place(relx=0.1, rely=0.2)
                            ctx_2 = CTkSwitch
                            
                            th.Thread(target=set_settings_lang_for_user).start()
                            winset.mainloop()
                    def rename():
                        def add_change_rename():
                            get1 = entry.get()
                            if get1 == "":
                                Messagebox.show_error(msglang, "Error!")
                                win.grab_set()
                                win.focus_set()
                            elif len(get1) > 20:
                                Messagebox.show_error(msglang1, "Error!")
                                win.grab_set()
                                win.focus_set()
                            elif len(get1) < 4:
                                Messagebox.show_error(msglang2, "Error!")
                                win.grab_set()
                                win.focus_set()
                            else:
                                public.set("MicroSoftware", "username", f"{get1}")
                                with open(f"{path}/system/settings.ini", "w") as set_new_n:
                                    public.write(set_new_n)
                                messagebox.showinfo("Succefull!", f"{done}.")
                                set_new_name = configparser.ConfigParser()
                                set_new_name.read(f"{PATH}/system/settings.ini")
                                get_name = set_new_name.get("MicroSoftware", "username")
                                if get == "English":
                                    username_label_view.configure(text=f"Hello {get_name}.")
                                elif get == "Italiano":
                                    username_label_view.configure(text=f"Ciao {get_name}.")
                                elif get == "Español":
                                    username_label_view.configure(text=f"Hola {get_name}.")
                                win.destroy()

                        get = langvar.get()
                        if get == "English":
                            langset = "Change the name."
                            msglang = "Name is empty please enter a valid name. Try again."
                            msglang1 = "The name must be less than 20 characters maximum. Try again."
                            msglang2 = "The name must be at least 4 characters long. Try again."
                            cancell = "Cancel"
                            done = "Done"
                        elif get == "Italiano":
                            langset = "Cambia il nome."
                            msglang = "Il nome è vuoto, inserisci un nome valido. Riprova."
                            msglang1 = "Il nome deve essere minore di 20 caratteri come massimo. Riprova."
                            msglang2 = "Il nome deve superare almeno 4 caratteri. Riprova."
                            cancell = "Annulla"
                            done = "Fatto"
                        elif get == "Español":
                            langset = "Cambia el nombre."
                            msglang = "El nombre está vacío, ingrese un nombre válido. Intentar otra vez."
                            msglang1 = "El nombre debe tener menos de 20 caracteres como máximo. Intentar otra vez."
                            msglang2 = "El nombre debe tener al menos 4 caracteres. Intentar otra vez."
                            cancell = "Cancellar"
                            done = "Hecho"
                        win = Toplevel()
                        win.focus_set()
                        win.config(background="white")
                        win.iconbitmap(f"{PATH}/system/src/icon.ico")
                        win.title(langset)
                        win.resizable(False, False)
                        win.update()
                        win.iconbitmap(f"{PATH}/system/src/icon.ico")
                        winwidth = 300
                        winheight = 200
                        winx = (win.winfo_screenwidth() // 2 - winwidth // 2)
                        winy = (win.winfo_screenheight() // 2 - winheight // 2)
                        win.geometry(f"{winwidth}x{winheight}+{winx}+{winy}")
                        label_ctk = CTkLabel(win, text=langset, font=("Roboto", 16), text_color="red")
                        label_ctk.place(relx=0.5, rely=0.235, anchor=CENTER)
                        entry = Entry(win, width=28)
                        entry.place(relx=0.5, rely=0.55, anchor=CENTER)
                        cancel_button = CTkButton(win, text=cancell, width=10, command=lambda: win.destroy())
                        cancel_button.place(relx=0.4, rely=0.74, anchor=CENTER)
                        done_button = CTkButton(win, text=done, width=10, command=add_change_rename)
                        done_button.place(relx=0.6, rely=0.74, anchor=CENTER)
                        entry.bind("<Return>", lambda event: add_change_rename())
                        win.bind("<Escape>", lambda event: win.destroy())
                        win.grab_set()
                        win.mainloop()
                    def reset_system():
                        get = langvar.get()
                        if get == "English":
                            set_lang = "Are you sure you reset MicroSoftware? If you reset it then all data and settings will be reset."
                            pass_lang = "Process cancelled."
                        elif get == "Italiano":
                            set_lang = "Sei sicuro di resettare MicroSoftware? Se lo resetti allora tutti i dati e le  impostazioni verranno resettate."
                            pass_lang = "Processo annullato."
                        elif get == "Español":
                            set_lang = "¿Estás seguro de que reiniciaste MicroSoftware? Si lo restablece, todos los datos y configuraciones se restablecerán."
                            pass_lang = "Proceso cancelado."
                        msg = messagebox.askyesno("Warning!", set_lang)
                        if msg:
                            with open(f'{PATH}/system/settings.ini', "wb") as reset_settings:
                                reset_settings.write("""[MicroSoftware]
enable-splash-screen = True
set-trasparency = 1
enable-closing-message = True
language-set = English
username = None
custom_image_path = None
user_icon_set = default_m

[Root]
exist_old_user = False
version = 5.60.2v""".encode())
                        else:
                            Messagebox.show_info(pass_lang, "Process cancelled.")
                    def update_core_ms():
                        def exist_wifi() -> bool:
                            try:
                                socket.create_connection(("8.8.8.8", 53), timeout=2)
                                return True
                            except OSError:
                                return False
                        if exist_wifi():
                                def translate_b():
                                    get = langvar.get()
                                    if get == "English":
                                        wxcore_build_label.configure(text=f"New build available")
                                        wxcore_build_label_b.configure(text=f'New build available: "{windb_last_version_for_ms5602v.pop("version/build")}".')
                                        options_label_b.config(text="Options:")
                                        update_now_button_b.configure(text="Update")
                                        view_information_release_b.configure(text="Release notes")
                                        update_later_b.configure(text="Update later")
                                    elif get == "Italiano":
                                        wxcore_build_label.configure(text="Nuovo build disponibile")
                                        wxcore_build_label_b.configure(text=f'Nuova build disponibile: "{windb_last_version_for_ms5602v.pop("version/build")}".')
                                        options_label_b.config(text="Opzioni:")
                                        update_now_button_b.configure(text="Aggiorna")
                                        view_information_release_b.configure(text="Note di rilascio")
                                        update_later_b.configure(text="Aggiorna dopo")
                                    elif get == "Español":
                                        wxcore_build_label.configure(text="Nueva build disponible")
                                        wxcore_build_label_b.configure(text=f'Nueva build disponible: "{windb_last_version_for_ms5602v.pop("version/build")}".')
                                        options_label_b.config(text="Opciones:")
                                        update_now_button_b.configure(text="Actualizar")
                                        view_information_release_b.configure(text="Notas de lanzamiento")
                                        update_later_b.configure(text="Actualizar más tarde")
                                def translate_a():
                                    get = langvar.get()
                                    if get == "English":
                                        wxcore_update_label.configure(text=f"New update available")
                                        wxcore_version_label.configure(text=f'New version available: "{windb_last_version_for_ms5602v.pop("version/build")}".')
                                        options_label.config(text="Options:")
                                        update_now_button.configure(text="Update")
                                        view_information_release.configure(text="Release notes")
                                        update_later.configure(text="Update later")
                                    elif get == "Italiano":
                                        wxcore_update_label.configure(text="Nuovo aggiornamento disponibile")
                                        wxcore_version_label.configure(text=f'Nuova versione disponibile: "{windb_last_version_for_ms5602v.pop("version/build")}".')
                                        options_label.config(text="Opzioni:")
                                        update_now_button.configure(text="Aggiorna")
                                        view_information_release.configure(text="Note di rilascio")
                                        update_later.configure(text="Aggiorna dopo")
                                    elif get == "Español":
                                        wxcore_update_label.configure(text="Nueva actualización disponible")
                                        wxcore_version_label.configure(text=f'Nueva versión disponible: "{windb_last_version_for_ms5602v.pop("version/build")}".')
                                        options_label.config(text="Opciones:")
                                        update_now_button.configure(text="Actualizar")
                                        view_information_release.configure(text="Notas de lanzamiento")
                                        update_later.configure(text="Actualizar más tarde")
                                def close_window_b():
                                    new_build_frame_core.destroy()
                                    root.update()
                                    root.update_idletasks()
                                    root.unbind("<Escape>")
                                def close_window():
                                    new_update_frame_core.destroy()
                                    root.update()
                                    root.update_idletasks()
                                    root.unbind("<Escape>")
                                def release():
                                    get_url = sel_cv.get().to_dict().pop("release_url")
                                    webbrowser.open(get_url)

                                
                                

                                current_version_core = "5.60.2v"
                                current_build_core = "1"
                                sel_project = db.collection("projects")
                                sel_msf = sel_project.document("MicroSoftware")
                                sel_current = sel_msf.collection("current_version")
                                sel_cv = sel_current.document(current_version_core)
                                windb_last_version_for_ms5602v = sel_cv.get().to_dict()
                                version = sel_cv.get().to_dict().pop("is_build_or_version")
                                print(windb_last_version_for_ms5602v)
                                if windb_last_version_for_ms5602v.pop("new"):   
                                    if version == "version":
                                        if version > current_version_core:
                                            new_update_frame_core = CTkFrame(root, width=500, height=500, fg_color="#00A0E6", border_width=2, border_color="black", corner_radius=0)
                                            new_update_frame_core.place(relx=0.5, rely=0.5, anchor=CENTER)
                                            new_update_frame_core.grab_set()
                                            close_image_loader = CTkImage(Image.open(f"{path}/system/src/close_icon.png"), size=(35, 35))
                                            close_frame_button = CTkButton(new_update_frame_core, text="", image=close_image_loader, fg_color="transparent", hover=False, command=close_window, width=10, height=10, corner_radius=365)
                                            close_frame_button.place(relx=0.94, rely=0.06, anchor=CENTER)
                                            wxcore_update_label = CTkLabel(new_update_frame_core, text="", font=("Roboto", 25), text_color="white")
                                            wxcore_update_label.place(relx=0.1, rely=0.1)
                                            wxcore_version_label = CTkLabel(new_update_frame_core, text="", font=("Roboto", 13.5), text_color="black")
                                            wxcore_version_label.place(relx=0.1, rely=0.2)
                                            
                                            view_frame = CTkFrame(new_update_frame_core, width=200, height=320, border_color="white", border_width=1, fg_color="transparent")
                                            view_frame.place(relx=0.1, rely=0.31)
                                            options_label = Label(view_frame, text="", background="#00A0E6", foreground="black")
                                            options_label.place(relx=0.1, rely=0.1)
                                            update_image_loader = CTkImage(Image.open(f"{PATH}/system/src/update_image.png"), size=(190, 190))
                                            free_label = CTkLabel(new_update_frame_core, text="", image=update_image_loader)
                                            free_label.place(relx=0.59, rely=0.37)
                                            update_now_button = CTkButton(view_frame, text="", fg_color="#00E34C", hover_color="#00DA49", width=150, text_color="black", command=None)
                                            update_now_button.place(relx=0.1, rely=0.2)

                                            view_information_release = CTkButton(view_frame, text="", fg_color="white", hover_color="#EAECEE", width=150, text_color="black", command=release)
                                            view_information_release.place(relx=0.1, rely=0.3)

                                            update_later = CTkButton(view_frame, text="", fg_color="#FF2A00", hover_color="#ff0d00", width=150, text_color="white", command=close_window)
                                            update_later.place(relx=0.1, rely=0.4)
                                            
                                            root.bind("<Escape>", lambda event: close_window())
                                            th.Thread(target=translate_a).start()
                                        else:
                                            pass
                                    elif version == "build":
                                        if version > current_build_core:
                                            new_build_frame_core = CTkFrame(root, width=500, height=500, fg_color="#00A0E6", border_width=2, border_color="black", corner_radius=0)
                                            new_build_frame_core.place(relx=0.5, rely=0.5, anchor=CENTER)
                                            new_build_frame_core.grab_set()
                                            close_image_loader_b = CTkImage(Image.open(f"{path}/system/src/close_icon.png"), size=(35, 35))
                                            close_frame_button_b = CTkButton(new_build_frame_core, text="", image=close_image_loader_b, fg_color="transparent", hover=False, command=close_window_b, width=10, height=10, corner_radius=365)
                                            close_frame_button_b.place(relx=0.94, rely=0.06, anchor=CENTER)
                                            wxcore_build_label = CTkLabel(new_build_frame_core, text="", font=("Roboto", 25), text_color="white")
                                            wxcore_build_label.place(relx=0.1, rely=0.1)
                                            wxcore_build_label_b = CTkLabel(new_build_frame_core, text="", font=("Roboto", 13.5), text_color="black")
                                            wxcore_build_label_b.place(relx=0.1, rely=0.2)
                                            
                                            view_frame_b = CTkFrame(new_build_frame_core, width=200, height=320, border_color="white", border_width=1, fg_color="transparent")
                                            view_frame_b.place(relx=0.1, rely=0.31)
                                            options_label_b = Label(view_frame_b, text="", background="#00A0E6", foreground="black")
                                            options_label_b.place(relx=0.1, rely=0.1)
                                            update_image_loader_b = CTkImage(Image.open(f"{PATH}/system/src/update_image.png"), size=(190, 190))
                                            free_label_b = CTkLabel(new_build_frame_core, text="", image=update_image_loader_b)
                                            free_label_b.place(relx=0.59, rely=0.37)
                                            update_now_button_b = CTkButton(view_frame_b, text="", fg_color="#00E34C", hover_color="#00DA49", width=150, text_color="black", command=None)
                                            update_now_button_b.place(relx=0.1, rely=0.2)

                                            view_information_release_b = CTkButton(view_frame_b, text="", fg_color="white", hover_color="#EAECEE", width=150, text_color="black", command=None)
                                            view_information_release_b.place(relx=0.1, rely=0.3)

                                            update_later_b = CTkButton(view_frame_b, text="", fg_color="#FF2A00", hover_color="#ff0d00", width=150, text_color="white", command=close_window_b)
                                            update_later_b.place(relx=0.1, rely=0.4)
                                            
                                            root.bind("<Escape>", lambda event: close_window_b())
                                            th.Thread(target=translate_b).start()
                                        else:
                                            pass
                                else:
                                    pass
                            
                        else:
                            pass
                        

                    def check_time_and_date():
                        timew = tm.strftime("%H:%M:%S")
                        datew = tm.strftime("%d/%m/%Y")
                        view_time_and_date_label.configure(text=f"{timew}\n{datew}")
                        view_time_and_date_label.after(1000, check_time_and_date)
                    class set_language():
                        def __init__(self, *args) -> None:
                            try:
                                get = langvar.get()
                                if get == "English":
                                    username_label_view.configure(text=f"Hello {get_first_name}.")
                                    settings_button.configure(text="Settings")
                                    info_button.configure(text="Information")
                                    exit_button.configure(text="Exit")
                                    rename_button.config(text="Rename")
                                    end_date_meter.configure(subtext="Day left", textright="")
                                elif get == "Italiano":
                                    username_label_view.configure(text=f"Ciao {get_first_name}.")
                                    settings_button.configure(text="Impostazioni")
                                    info_button.configure(text="Informazioni")
                                    exit_button.configure(text="Esci")
                                    rename_button.configure(text="Rinomina")
                                    end_date_meter.configure(subtext="Giorni rimasti", textright="")
                                elif get == "Español":
                                    username_label_view.configure(text=f"Hola {get_first_name}.")
                                    rename_button.config(text="Rebautizar")
                                    settings_button.configure(text="Ajustes")
                                    info_button.configure(text="Información")
                                    exit_button.configure(text="Salir")
                                    rename_button.config(text="Rebautizar")
                                    end_date_meter.configure(subtext="Días restantes", textright="")
                            except Exception:
                                pass
                    root.update()
                    root.update_idletasks()
                    conf = configparser.ConfigParser()
                    conf.read(f"{PATH}/system/settings.ini")
                    get_first_name = conf.get("MicroSoftware", "username")
                    style = Style()
                    #style.configure("Test.Core.TMeter", background="white")
                    style.configure("Separes.TSeparator", background="red")
                    style.configure("Dashboard.System.Reset.TButton", foreground="white", bootstyle="warning", font=("Roboto", 15))
                    calculate_width_for_user_frame_menu = (root.winfo_width() - 1040)
                    user_frame_menu = CTkFrame(root, width=calculate_width_for_user_frame_menu, height=root.winfo_height(), fg_color="white", corner_radius=0)
                    user_frame_menu.pack(side=LEFT)
                    dashboard_frame = CTkFrame(root, corner_radius=0, fg_color="white")
                    dashboard_frame.pack(expand=True, fill=BOTH, side=RIGHT)
                    # User frame widgets
                    try:
                        timew = tm.strftime("%H:%M:%S")
                        datew = tm.strftime("%d/%m/%Y")
                        load_date_time_image = CTkImage(Image.open(f"{path}/system/src/date_time_image.jpg"), size=(40, 40))
                        load_date_time_image_label = CTkLabel(user_frame_menu, text="", image=load_date_time_image)
                        load_date_time_image_label.place(relx=0.35, rely=0.05, anchor=CENTER)
                        view_time_and_date_label = Label(user_frame_menu, text=f"{timew}\n{datew}", font=("Roboto", 10), justify="center")
                        view_time_and_date_label.place(relx=0.6, rely=0.05, anchor=CENTER)
                    except Exception:
                        pass
                    try:
                        get_img_model = conf.get("MicroSoftware", "user_icon_set")
                        if get_img_model == "default_m":
                            user_image = CTkImage(Image.open(f"{PATH}/system/src/user_m_default.png"), size=(165, 165))
                        elif get_img_model == "image_m_1":
                            user_image = CTkImage(Image.open(f"{PATH}/system/src/user_m_1.png"), size=(165, 165))
                        elif get_img_model == "default_f":
                            user_image = CTkImage(Image.open(f"{path}/system/src/user_f_default.png"), size=(165, 165))
                        elif get_img_model == "image_f_1":
                            user_image = CTkImage(Image.open(f"{path}/system/src/user_f_1.png"), size=(165, 165))
                        elif get_img_model == "custom":
                            custom_image = conf.get("MicroSoftware", "custom_image_path")
                            user_image = CTkImage(Image.open(f"{custom_image}"), size=(165, 165))
                        else:
                            user_image = CTkImage(Image.open(f"{PATH}/system/src/user_m_default.png"), size=(165, 165))
                    except Exception as error:
                        Messagebox.show_error(f"Image load error: {error}")
                    try:
                        img_view_user_image = CTkLabel(user_frame_menu, text="", image=user_image)
                        img_view_user_image.place(relx=0.5, rely=0.2, anchor=CENTER)
                    except Exception:
                        pass

                    username_label_view = CTkLabel(user_frame_menu, text="", font=("Roboto", 15), text_color="black")
                    username_label_view.place(relx=0.5, rely=0.35, anchor=CENTER)
                    separe_user_info = Separator(user_frame_menu, orient="horizontal", bootstyle="info", style="Separe.TSeparator")
                    separe_user_info.place(relwidth=0.8, relx=0.5, rely=0.41, anchor=CENTER)
                    try:
                        adv_image_loader = CTkImage(Image.open(f"{PATH}/system/src/advanced_console_image.png"), size=(30, 30))
                        adv_button = CTkButton(user_frame_menu, text="Ultimate Tools", image=adv_image_loader, fg_color="transparent", hover_color="#EAECEE", command=adv, height=45, text_color="black", compound=TOP)
                        adv_button.place(relx=0.5, rely=0.47, anchor=CENTER)
                    except  Exception:
                        pass
                    try:
                        info_image_loader = CTkImage(Image.open(f"{path}/system/src/info_image.png"), size=(30, 30))
                        info_button = CTkButton(user_frame_menu, text="", command=view_information, image=info_image_loader, hover_color="#EAECEE", height=45, fg_color="transparent", text_color="black", compound=TOP)
                        info_button.place(relx=0.5, rely=0.56, anchor=CENTER)
                    except Exception:
                        pass
                    try:
                        settings_image_loader = CTkImage(Image.open(f"{PATH}/system/src/settings_image.png"), size=(30, 30))
                        settings_button = CTkButton(user_frame_menu, text="", command=settings, fg_color="transparent", hover_color="#EAECEE", image=settings_image_loader, height=45, text_color="black", compound=TOP)
                        settings_button.place(relx=0.5, rely=0.67, anchor=CENTER)
                    except Exception:
                        pass
                    try:
                        exit_image_loader = CTkImage(Image.open(f"{PATH}/system/src/exit_image.png"), size=(30, 30))
                        exit_button = CTkButton(user_frame_menu, text="", height=45, hover_color="#EAECEE", fg_color="transparent", image=exit_image_loader, command=exit_configure, text_color="black", compound=TOP)
                        exit_button.place(relx=0.5, rely=0.78, anchor=CENTER)
                    except Exception:
                        pass
                    root.update()
                    root.update_idletasks()
                    copyright = Label(user_frame_menu, text="© Copyright 2022 - 2023 Informatic365", font=("Roboto", 9))
                    copyright.place(relx=0.5, rely=0.98, anchor=CENTER)
                    # Dashboard frame widgets
                    first_frame_on_dashboard = CTkFrame(dashboard_frame, width=root.winfo_width(), height=60, fg_color="#00AEFF", corner_radius=0)
                    first_frame_on_dashboard.pack(side=TOP)
                    # first_frame_on_dashboard widgets
                    msf_title_dashboard = Label(first_frame_on_dashboard, text="MicroSoftware 5.60.2v Enterprise", font=("Roboto", 20), foreground="white", background="#00AEFF")
                    msf_title_dashboard.place(relx=0.2, rely=0.5, anchor=CENTER)
                    rename_button = Button(first_frame_on_dashboard, text="", style="Dashboard.System.Reset.TButton", command=rename, width=5.5)
                    rename_button.place(relx=0.83, rely=0.5, anchor=CENTER)
                    reset_button_to_reset_microsoftware = Button(first_frame_on_dashboard, text="Reset", command=reset_system, style="Dashboard.System.Reset.TButton", width=5)
                    reset_button_to_reset_microsoftware.place(relx=0.93, rely=0.5, anchor=CENTER)
                    Separator(dashboard_frame, orient="vertical").place(relx=0.001, rely=0.125, relheight=0.825)
                    label_1 = CTkLabel(dashboard_frame, text="Dashboard:", text_color="red", font=("Roboto", 25, "bold"))
                    label_1.place(relx=0.01, rely=0.1)
                    end_date_meter = Meter(dashboard_frame, metersize=180, amounttotal=730, stripethickness=10, subtextfont="-size 12", textright="-size 14 -weight bold", subtextstyle=DARK)
                    end_date_meter.place(relx=0.71, rely=0.11)
                    date_end = datetime.strptime("15/01/2026", "%d/%m/%Y")
                    now_time = datetime.now()
                    c_end_time = date_end - now_time
                    get_total = c_end_time.days
                    end_date_meter.configure(amountused=get_total)




                    # Language-set widgets
                    langvar = StringVar()
                    get_lang_ini = conf.get("MicroSoftware", "language-set")
                    if get_lang_ini == "English":
                        langvar.set("English")
                    elif get_lang_ini == "Italiano":
                        langvar.set("Italiano")
                    elif get_lang_ini == "Spanish":
                        langvar.set("Español")
                    else:
                        langvar.set("English")
                    
                    # Binds
                    root.bind("<Control-i>", lambda event: settings())
                    root.bind("<Control-I>", lambda event: settings())
                    root.bind("<F1>", lambda event: view_information())
                    # Threads
                    #th.Thread(target=update_root).start()
                    th.Thread(target=update_core_ms).start()
                    th.Thread(target=check_time_and_date).start()
                    th.Thread(target=set_language).start()
            def register():
                try:
                    save_name = username_entry.get()
                    if save_name == "Name:":
                        error_label.config(text="Invalid name or empty name. Try again.")
                        try:
                            root.after(2000, lambda: error_label.config(text=""))
                        except Exception:
                            pass
                    elif len(save_name) > 20:
                        error_label.config(text="Name longer than 20 characters or the name is empty or invalid. Try again.")
                        username_entry.delete(0, END)
                        try:
                            root.after(2000, lambda: error_label.config(text=""))
                        except Exception:
                            pass
                    else:
                        public.set("MicroSoftware", "username", f"{save_name}")
                        public.set("Root", "exist_old_user", "True")
                        with open(f"{path}/system/settings.ini", "w") as set_all:
                            public.write(set_all)
                        __init_app__(username=save_name)
                except Exception as error:
                    messagebox.showerror("Error", f"Error code: {error}.")
            def __init_app__(username):
                def start_animation():
                    try:
                        def start_open():
                            for iw in root.winfo_children():
                                iw.destroy()
                            home(username)
                        for i in range(len(text__)+1):
                            welcome_user_label.configure(text=text__[:i])
                            tm.sleep(0.05)
                        root.after(1000, start_open)
                    except Exception:
                        pass
                text__ = f'Welcome "{username}"'
                sys_login_frame = CTkFrame(root, width=root.winfo_width(), height=root.winfo_height(), fg_color="white", corner_radius=0)
                sys_login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                welcome_user_label = CTkLabel(sys_login_frame, text="", font=("Consolas bold", 30), text_color="#00A6FF")
                welcome_user_label.place(relx=0.5, rely=0.4, anchor=CENTER)
                try:
                    th.Thread(target=start_animation).start()
                except Exception:
                    pass

            def create_random_username():
                def sys_random_username():
                    choice = random.randint(1, 4)
                    if choice == 1:
                        random_char = random.choice(string.ascii_letters)
                    else:
                        random_char = str(random.randint(0, 9))
                    return random_char
                def generate_user_string():
                    user_string = "user#"
                    for _ in range(4):
                        user_string += sys_random_username()
                    user_string += sys_random_username()
                    user_string += sys_random_username()
                    return user_string
                win_user = generate_user_string()
                username_entry.config(foreground="black")
                username_entry.delete(0, END)
                username_entry.insert(0, win_user)
            root.overrideredirect(0)
            root.protocol("WM_DELETE_WINDOW", exit_configure)
            try:
                for wroot in root.winfo_children():
                    wroot.destroy()
            except Exception:
                pass
            if public.getboolean("Root", "exist_old_user"):
                try:
                    username = public.get("MicroSoftware", "username")
                    if len(username) > 20:
                        winname = create_random_username()
                        public.set("MicroSoftware", "username", f"{winname}")
                        with open(f"{path}/system/settings.ini", "w") as set_new_username:
                            public.write(set_new_username)
                        __init_app__(username=username)
                    else:
                        __init_app__(username=username)
                except Exception:
                    winname = create_random_username()
                    public.set("MicroSoftware", "username", f"{winname}")
                    with open(f"{path}/system/settings.ini", "w") as set_new_username:
                        public.write(set_new_username)
                    __init_app__(username=username)
            else:
                def entryon():
                    if username_entry.get() == text:
                        username_entry.delete(0, END)
                        username_entry.config(foreground="black")
                def entryoff():
                    if username_entry.get() == "":
                        username_entry.insert(0, text)
                        username_entry.config(foreground="gray")
                styles = Style()
                styles.configure("System.Entry.Username.TEntry", bootstyle="default")
                styles.configure("Generate.Name.TButton", font=("Roboto", 8))
                styles.configure("Error.Void.TLabel", bootstyle="error", foreground="red")
                main_frame = CTkFrame(master=root, border_width=1, border_color="white", fg_color="transparent")
                main_frame.pack(fill=BOTH, expand=True)
                iframe = CTkFrame(main_frame, fg_color="#00A6FF", corner_radius=0)
                iframe.pack(expand=True, side=LEFT, fill=BOTH)
                lframe = CTkFrame(main_frame, fg_color="white", corner_radius=0)
                lframe.pack(side=RIGHT, fill=BOTH, expand=True)
                image_1 = CTkImage(Image.open(f"{path}/system/src/icon.ico"), size=(400, 400))
                image_label = CTkLabel(iframe, image=image_1, text="")
                image_label.place(relx=0.5, rely=0.5, anchor=CENTER)
                i_title_label = CTkLabel(iframe, text="MicroSoftware 5.60.2v", font=("Consolas bold", 30), text_color="white")
                i_title_label.place(relx=0.05, rely=0.05)
                l_title_label = CTkLabel(lframe, text="MicroSoftware Login", font=("Roboto", 33), text_color="#00A6FF")
                l_title_label.pack(pady=79)
                CTkLabel(lframe, text="Welcome To MicroSoftware.\nPlease insert your name to continue", font=("Roboto", 16), text_color="red").place(relx=0.5, rely=0.19, anchor=CENTER)
                label_username = CTkLabel(lframe, text="Please enter your name:", font=("Roboto", 15))
                label_username.place(relx=0.3025, rely=0.4)
                username_entry = Entry(lframe, width=38, style="System.Entry.Username.TEntry")
                username_entry.place(relx=0.3, rely=0.44)
                text = "Name:"
                username_entry.insert(0, text)
                username_entry.bind("<FocusIn>", lambda event: entryon())
                username_entry.bind("<FocusOut>", lambda event: entryoff())
                generate_name_button = Button(lframe, text="Generate Name", style="Generate.Name.TButton", width=14, command=create_random_username)
                generate_name_button.place(relx=0.5, rely=0.51, anchor=CENTER)
                login_button = Button(lframe, text="Next", style="Generate.Name.TButton", width=14, command=register)
                login_button.place(relx=0.67, rely=0.67)
                error_label = Label(lframe, text="", style="Error.Void.TLabel")
                error_label.place(relx=0.5, rely=0.55, anchor=CENTER)

    if os.path.exists(f"{path}/system/settings.ini"):
        pass
    else:
        with open(f"{PATH}/system/settings.ini", "wb") as create_settings:
            create_settings.write("""[MicroSoftware]
enable-splash-screen = True
set-trasparency = 1
enable-closing-message = True
language-set = English
username = None
custom_image_path = None
user_icon_set = default_m

[Root]
exist_old_user = False
version = 5.60.2v""".encode())
    public = configparser.ConfigParser()
    public.read(f"{path}/system/settings.ini")
    root = Window(title="MicroSoftware Enterprise 5.60.2v")
    get_t = public.get("MicroSoftware", "set-trasparency")
    if get_t == "1":
        root.attributes("-alpha", 1)
    elif get_t == "0.9":
        root.attributes("-alpha", 0.9)
    elif get_t == "0.8":
        root.attributes("-alpha", 0.8)
    elif get_t == "0.7":
        root.attributes("-alpha", 0.7)
    elif get_t == "0.6":
        root.attributes("-alpha", 0.6)
    elif get_t == "0.5":
        root.attributes("-alpha", 0.5)
    elif get_t == "0.4":
        root.attributes("-alpha", 0.4)
    elif get_t == "0.3":
        root.attributes("-alpha", 0.3)
    elif get_t == "0.2":
        root.attributes("-alpha", 0.2)
    elif get_t == "0.1":
        root.attributes("-alpha", 0.1)
    else:
        root.attributes("-alpha", 1)
    
    root.overrideredirect(1)
    try:
        root.iconbitmap(f"{path}/system/src/icon.ico")
    except Exception:
        pass
    boolean = public.getboolean
    width = 1310
    height = 720
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw // 2 - width // 2)
    y = (sh // 2  - height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)
    root.deiconify()
    try:
        def notexit():
            pass
        root.protocol("WM_DELETE_WINDOW", notexit)
        end_date = "15/01/2026"
        current_time = datetime.now()
        current = current_time.strftime("%d/%m/%Y")
        end_date_obj = datetime.strptime(end_date, "%d/%m/%Y")
        current_date_obj = datetime.strptime(current, "%d/%m/%Y")
        if current_date_obj >= end_date_obj:
            root.protocol("WM_DELETE_WINDOW", exit_configure)
            end_frame = CTkFrame(root, fg_color="white")
            end_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
            end_label = CTkLabel(end_frame, text="This version of MicroSoftware is no longer supported and no longer in use.\nPlease download and install the latest version of MicroSoftware.", text_color="red", font=("Arial", 30))
            end_label.place(relx=0.5, rely=0.38, anchor=CENTER)
            end_button = CTkButton(master=end_frame, text="Exit", command=lambda: sys.exit(), width=70)
            end_button.place(relx=0.4, rely=0.525, anchor=CENTER)
        else:
            if boolean("MicroSoftware", "enable-splash-screen"):
                def start_animation():
                    try:
                        for i in range(len(welc_label_text)+1):
                            welc_label.config(text=welc_label_text[:i])
                            tm.sleep(0.05)
                        deslabel.configure(text="Next generation of MicroSoftware")
                    except Exception:
                        pass
                wimage = CTkImage(Image.open(f"{path}/system/src/icon.ico"), size=(500, 500))
                label = CTkLabel(root, image=wimage, text="")
                label.place(relx=0.5, rely=0.5, anchor=CENTER)
                welc_label = Label(master=root, text="", font=("Consolas bold", 48))
                welc_label.place(relx=0.1, rely=0.1)
                welc_label_text = "MicroSoftware 5.60.2v"
                deslabel = CTkLabel(root, text="", font=("Consolas bold", 20), text_color="#00A6FF")
                deslabel.place(relx=0.2, rely=0.21)
                go_on = th.Thread(target=start_animation)
                go_on.start()
                root.bind("<F1>", lambda event: checking())
                set_start_timer = root.after(3500, checking)
            else:
                go()
    except Exception as error:
        root.protocol("WM_DELETE_WINDOW", exit_configure)
        frame_error = CTkFrame(root, fg_color="white", border_color="black", border_width=1.5)
        frame_error.pack(padx=7, pady=7, fill="both", expand=True)
        label_sys_error = CTkLabel(frame_error, text="Oops! There was an error.", font=("Roboto", 35), text_color="red")
        label_sys_error.pack(pady=75)
        label_error = CTkLabel(frame_error, text=f"Fatal error: {error}", font=("Roboto", 17), text_color="red")
        label_error.pack(pady=75)
    root.mainloop()
