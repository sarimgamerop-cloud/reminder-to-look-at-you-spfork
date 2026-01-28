import asyncio
from desktop_notifier import DesktopNotifier, Icon, Button
from pathlib import Path
from time import sleep


project_root = Path(__file__).parent  # give the location of folder

alert_icon = project_root / "assets" / "alert.png"
water_bottle = project_root / "assets" / "water_bottle.png"
notifier = DesktopNotifier()


# This Func gonna send a notification based on paramaters
async def send(title: str, message: str, icon: Path):
    while True:
        await asyncio.sleep(4)
        await notifier.send(
            title=title,
            message=message,
            icon=Icon(icon),
            buttons=[
                Button(title="Ok", on_pressed=print("Drinked")),
                Button(title="skip", on_pressed=print("Skiped")),
            ],
        )


# print(project_root)

if __name__ == "__main__":
    asyncio.run(
        send("There is Still Water in this world!", "Drink Water Sir!", water_bottle)
    )
