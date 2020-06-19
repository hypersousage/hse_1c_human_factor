# Human factor implementation for traffic simulation

Implementation of the human factor affecting the behavior of the machine in traffic conditions. The implementation of the relationship of human factors from other conditions.

## Authors

* **Timur Vankov** - *Team lead* - [timurvankov](https://github.com/timurvankov)
* **Sergey Petrovich** - *Developer-researcher* - [serp404](https://github.com/serp404)
* **Maxim Minchenock** - *Developer-researcher* - [hypersousage](https://github.com/hypersousage)
* **Sabina Dayanova** - *Researcher* - [sabinadayanova](https://github.com/sabinadayanova)
* **Maria Shkolnik** - *Researcher* - [mashaashkolnik](https://github.com/mashaashkolnik)
* **Nikita Starichkov** - *Mentor* - [demist](https://github.com/demist)

## Run simulation

1. Install Pyro and Python (version grater than or equal to 3.6) 
2. Download SUMO [click here!](https://sumo.dlr.de/docs/Installing.html) (linux preferably)
3. Clone this rep to `/sumo/tools`
4. Run this `chmod ugo+x make.sh` in `/hse_1c_human_factor`
5. Run `./make.sh` for run only 1 simulation and `./make.sh 2` for run 2 simulations in one time(run in `/hse_1c_human_factor`)
6. Set your desired values in web:
    - Age: integer from 17 to 100
    - Sex: 0 for men, 1 for women
    - Stress: float from 0 to 1
    - Children: bool (1 for yes)
    - Personality: phlegmatic, holeric, sanguine, melancholic
    - Phone: bool (1 for yes)
    - Higher Education: bool (1 for yes)
    - Driving under influence of alcohol: float from 0 to 1
    - Social Deviance: degree (0-weak impact, 1- average impact, 2-strong impact)
    - Foreigner: bool (1 for yes)
7. Edit another things:
    1. Choose the area of the map that you want
    2. Click the "Generate scenario" button
    3. In the new window set the "delay" value on 100 and click on the green triangle button (play)
    4. After the start you can change the quantity of cars by changing the "scale traffic".
