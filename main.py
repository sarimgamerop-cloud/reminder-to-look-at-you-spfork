import asyncio
from desktop_notifier import DesktopNotifier, Icon
from pathlib import Path




project_root = Path(__file__).parent  # give the location of folder

alert_icon = project_root / "assets" / "alert.png"
water_bottle = project_root / "assets" / "water_bottle.png"
notifier = DesktopNotifier()

# This Func gonna send a notification based on paramaters
def main(title:str,message:str ,icon:str):
    async def send():
        await notifier.send(
            title=title,
            message=message,
            icon=Icon(icon),
        )

    asyncio.run(send())

# print(project_root)

if __name__ == "__main__":
    main("this is tittle","this is message", alert_icon)