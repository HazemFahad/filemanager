from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "/Users/hazemfahad/Downloads"
dest_dir_music = "/Users/hazemfahad/Downloads/music"
dest_dir_pdf = "/Users/hazemfahad/Downloads/pdf"
dest_dir_videos = "/Users/hazemfahad/Downloads/videos"
dest_dir_images = "/Users/hazemfahad/Downloads/images"
dest_dir_documents = "/Users/hazemfahad/Downloads/documents"
dest_dir_installers = "/Users/hazemfahad/Downloads/installers"
dest_dir_zip = "/Users/hazemfahad/Downloads/zip"
dest_dir_excalidraw = "/Users/hazemfahad/Downloads/excalidraw"



def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

with scandir(source_dir) as entries:
    for entry in entries:
        name = entry.name
        dest = source_dir
        if name.endswith('.wav') or name.endswith('.mp3'):
            dest = dest_dir_music
            move_file(dest, entry, name)

        elif name.endswith('.mov') or name.endswith('.mp4'):
            dest = dest_dir_videos
            move_file(dest, entry, name)

        elif name.endswith('.pdf'):
            dest = dest_dir_pdf
            move_file(dest, entry, name)

        elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith(".png") or name.endswith(".PNG"):
            dest = dest_dir_images
            move_file(dest, entry, name)

        elif name.endswith('.doc') or name.endswith('.docx') or name.endswith(".xls"):
            dest = dest_dir_documents
            move_file(dest, entry, name)

        elif name.endswith('.dmg'):
            dest = dest_dir_installers
            move_file(dest, entry, name)

        elif name.endswith('.zip') or name.endswith('.rar'):
            dest = dest_dir_zip
            move_file(dest, entry, name)

        elif name.endswith('.excalidraw'):
            dest = dest_dir_excalidraw
            move_file(dest, entry, name)

        elif name.endswith('.excalidraw'):
            dest = dest_dir_excalidraw
            move_file(dest, entry, name)

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'
#     event_handler = LoggingEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     finally:
#         observer.stop()
#         observer.join()
