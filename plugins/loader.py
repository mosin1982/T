from plugins.base import TPlugin

def run_plugins(plugins: list[TPlugin], context: dict) -> list[dict]:
    outputs = []
    for plugin in plugins:
        outputs.append({
            "plugin": plugin.name,
            "version": plugin.version,
            "output": plugin.run(context),
        })
    return outputs
