uuh ill make a proper readme later. heres how to set the mod up

1. Get a copy of Pizza Tower and open the `data.win` with UndertaleModTool.
2. Go to Scripts > Run other script and run `InjectAP.csx`.
3. For the first prompt, select the folder with sprites (called Sprites here, but you can rename it).
4. For the second prompt, select the folder with code. Normally, you'd have both new and modified code already, but if this is your first time running this, you will likely only have the new scripts and patch files.
      - For `restore_diffs.py`, select the folder with the original code (by extracting the `data.win`), and then select the folder with the patch files. This should generate the modified code in a folder called `code`.
      - For `create_diffs.py`, select the folder with the original code, and then select the folder with the modified code. This should create patch files for modified code. Use this when publishing/sharing this mod to avoid potential legal issues.
5. You should be done now. Save the `data.win` and run the game through the [YYToolkit](https://github.com/Archie-osu/YYToolkit) [mod](https://github.com/BabyblueSheep/Pizza-Tower-AP) *(i might make both mods a monorepo in the future, not sure)*.
Also add the `english.txt` to the game's language file, or else the game will crash in some scenarios.