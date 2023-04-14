
import time

inst_display_name = "bk_inst_name"
data = {"inst_display_name":"234"}
data["inst_display_name"] = "$"+str({inst_display_name})
print(data)
