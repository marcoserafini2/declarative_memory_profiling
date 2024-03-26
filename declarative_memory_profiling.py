from cat.mad_hatter.decorators import tool, hook, plugin
from cat.log import log
from typing import Final

#key profile
wm_dm_profile_key: Final[str] = 'declarative_memory_profile'

@hook 
def before_rabbithole_insert_memory(doc, cat):

    if wm_dm_profile_key in cat.working_memory:
        # insert the profile name metadata on doc
        log.debug(f"Profile before insert memory {cat.working_memory[wm_dm_profile_key]}")
        doc.metadata["profile"] = cat.working_memory[wm_dm_profile_key]
    
    return doc 

@hook
def before_cat_recalls_declarative_memories(declarative_recall_config, cat):

    if wm_dm_profile_key in cat.working_memory:
        # filter memories using profile metadata 
        log.debug(f"Profile before recall memories {cat.working_memory[wm_dm_profile_key]}")
        declarative_recall_config["metadata"] = {"profile": cat.working_memory[wm_dm_profile_key] }

    return declarative_recall_config

@hook 
def agent_fast_reply(fast_reply, cat):

    log.info(f"Message {cat.working_memory['user_message_json']['text']}")

    if cat.working_memory["user_message_json"]["text"][:2] == "@p":
        #Change active profile 
        profile_name = cat.working_memory["user_message_json"]["text"].split(" ")[1]
        cat.working_memory[wm_dm_profile_key] = profile_name
        fast_reply["output"] = f"Set profile to '{profile_name}'"
    
    elif wm_dm_profile_key in cat.working_memory and cat.working_memory["user_message_json"]["text"] == "@c":
        #Return current active profile
        fast_reply["output"] = f"Active profile is '{cat.working_memory[wm_dm_profile_key]}'"

    elif wm_dm_profile_key not in cat.working_memory:
        #Print available commands
        commands = """
        No declarative memory profile selected. Commands available:
        [@p profile_name] - Set the active profile to profile_name
        [@c]              - Print active profile
        """
        fast_reply["output"] = commands

    return fast_reply

