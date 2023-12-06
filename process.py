from WorkerClass import Init_Data_File, WorkerDataLoader, DATA_STRUCT, DATA_PATH

Init_Data_File(DATA_PATH, DATA_STRUCT)
handler = WorkerDataLoader(DATA_PATH)
handler.add_user(name="Taro")
handler.add_user(name="Inoki")
handler.add_user(name="Shibata")
handler.remove_user(1)
