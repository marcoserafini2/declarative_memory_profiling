from cat.mad_hatter.decorators import tool, hook, plugin
from cat.log import log
from pydantic import BaseModel

class DeclarativeMemoryProfilingSettings(BaseModel):
    #TODO customize message
    no_profile_set_error: str = ""

@plugin
def settings_model():
    return DeclarativeMemoryProfilingSettings

@hook 
def before_rabbithole_insert_memory(doc, cat):

    if "declarative_memory_profile" in cat.working_memory:
        # insert the profile name metadata on doc
        log.debug(f"Profile before insert memory {cat.working_memory['declarative_memory_profile']}")
        doc.metadata["profile"] = cat.working_memory["declarative_memory_profile"]
    
    return doc 

@hook
def before_cat_recalls_declarative_memories(declarative_recall_config, cat):

    if "declarative_memory_profile" in cat.working_memory:
        # filter memories using profile metadata 
        log.debug(f"Profile before recall memories {cat.working_memory['declarative_memory_profile']}")
        declarative_recall_config["metadata"] = {"profile": cat.working_memory["declarative_memory_profile"] }

    return declarative_recall_config

@hook 
def agent_fast_reply(fast_reply, cat):

    if cat.working_memory["user_message_json"]["text"][:2] == "@p":
        #Change active profile 
        profile_name = cat.working_memory["user_message_json"]["text"].split(" ")[1]
        cat.working_memory["declarative_memory_profile"] = profile_name
        fast_reply["output"] = f"Set profile to '{profile_name}'"
    
    elif "declarative_memory_profile" not in cat.working_memory:

        commands = """
        No declarative memory profile selected. Commands available:
        [@p profile_name] - Set the active profile to profile_name
        [@c]              - Print active profile (Not implemented yet)
        """
        fast_reply["output"] = commands

    return fast_reply

