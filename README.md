# Human factor implementation for traffic simulation

Implementation of the human factor affecting the behavior of the machine in traffic conditions. The implementation of the relationship of human factors from other conditions.

## Authors

* **Timur Vankov** - *Team lead* - [timurvankov](https://github.com/timurvankov)
* **Sergey Petrovich** - *Developer-researcher* - [serp404](https://github.com/serp404)
* **Maxim Minchenock** - *Developer-researcher* - [hypersousage](https://github.com/hypersousage)
* **Sabina Dayanova** - *Researcher* - [sabinadayanova](https://github.com/sabinadayanova)
* **Maria Shkolnik** - *Researcher* - [mashaashkolnik](https://github.com/mashaashkolnik)
* **Nikita Starichkov** - *Mentor* - [demist](https://github.com/demist)

## Inctruction

1. Install Pyro and Python (version grater than or equal to 3.6) 
2. Download SUMO [click here!](https://sumo.dlr.de/docs/Installing.html) (linux preferably)
3. Download all of the "Factor" files into one directory "/sumo/tools" without any subdirectories (the easiest way to do this is to click the "Clone or Download" button)
4. Move "vtype_gen.py" and "factors.json" from "/hse-1c_human-factor/code" to the "/tools" directory
5. Replace "randomTrips.py" from "/tools" with "randomTrips.py" from "/code"
6. Set your desired values in "factors.json":
- Age: from 17 to 100
- Sex: 0 for men, 1 for women
- Stress: float (0-1)
- Children: bool (1 for yes)
- Personality: phlegmatic, holeric, sanguine, melancholic
- Phone: bool (1 for yes)
- Higher Education: bool (1 for yes)
- Driving under influence: float (0-1)
- Social Deviance: degree (0-weak impact, 1- average impact, 2-strong impact)
- Foreigner: bool (1 for yes)
7. Run the simulation (run the command "python3 osmWebWizard.py"):
- Choose the area of the map that you want
- Click the "Generate scenario" button
- In the new window set the "delay" value on 100 and click on the green triangle button (play)
