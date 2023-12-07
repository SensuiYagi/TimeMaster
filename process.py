from WorkerClass import Init_Data_File, WorkerDataLoader, DATA_STRUCT, DATA_PATH

Init_Data_File(DATA_PATH, DATA_STRUCT)
handler = WorkerDataLoader(DATA_PATH)
handler.add_user_id("yamada")
handler.add_user_id("Tanaka")
handler.add_user_id("yamada")



handler.remove_user(3)

handler.add_user_id("yamanaka")