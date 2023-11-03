using System.Linq;
using System.Text;
using System.Windows.Forms;
using System;
using System.IO;
using System.Threading.Tasks;
using UndertaleModLib.Util;


EnsureDataLoaded();

if (Data?.GeneralInfo?.DisplayName?.Content.ToLower() != "pizza tower")
{
    ScriptError("Script must be ran in Pizza Tower.");
    return;
}

if (!ScriptQuestion("Do you want to import Pizza Tower Archipelago?"))
{
    return;
}



// Change internal name
Data.Strings.First(s => s.Content == "PizzaTower_GM2").Content = "PizzaTower_AP";



/// Import sprites
bool importSprites = RunUMTScript(Path.Combine(ExePath, "Scripts", "Resource Repackers", "ImportGraphics.csx"));
if (!importSprites)
    throw new ScriptException("Unable to import sprites.");



// Import code
string importFolder = PromptChooseDirectory();
if (importFolder == null)
    throw new ScriptException("The import folder was not set.");

string[] dirFiles = Directory.GetFiles(importFolder);
if (dirFiles.Length == 0)
    throw new ScriptException("The selected folder is empty.");
else if (!dirFiles.Any(x => x.EndsWith(".gml")))
    throw new ScriptException("The selected folder doesn't contain any GML file.");

SyncBinding("Strings, Code, CodeLocals, Scripts, GlobalInitScripts, GameObjects, Functions, Variables", true);
await Task.Run(() => {
    foreach (string file in dirFiles)
    {
        ImportGMLFile(file, true, false, true);
    }
});
DisableAllSyncBindings();



ScriptMessage("All done!");