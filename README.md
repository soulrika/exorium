# exorium discord bot | Since 2020
----
### exorium information
exorium is a multifunctional bot used for many categories. The main aim for exorium was, and still is social commands. With a variety of commands and more being added regularly, we aim to ensure user experience to be at it's best and try to improve our commands as well as the bot as much as possible.

exorium started off as a small bot named Protogen, which was created by [BluewyDev](https://github.com/BluewyDev/) for own use. Later on the decision was made to give Protogen a new purpose: Social commands for [The Paw Kingdom](https://linktr.ee/pawkingdom). A while later the name was changed to ProtoPaw. Protopaw eventually moved to Heroku as host, where it was made public and [ChosenFate](https://github.com/Chosen-Fate) joined the team as developer. Shortly after [Etile](https://github.com/Etile0) provided us with a vps we could use to host Protopaw, a while after that, we changed the name to exorium.

---
### exorium team
- [BluewyDev](https://github.com/BluewyDev) - Creator, main developer and social media manager
- [ToothyDev](https://github.com/ToothyDev) - Main developer
- [Bench](https://github.com/Bench182) - Limited developer
- [Etile](https://github.com/Etile0) - Host and provider
---
### Contributions
Anyone is free to contribute to exorium as long as they follow the [Contribution guidelines](https://github.com/ThePawKingdom/exorium/blob/master/CONTRIBUTING.md). Contributions can be done through [forks](https://github.com/ThePawKingdom/exorium/network/members). In your fork you can edit, add and remove code. After you did that, you are always free to make a [pull request](https://github.com/ThePawKingdom/exorium/pulls/). They will then be reviewed by one of the [main developers](https://github.com/ThePawKingdom/exorium#exorium-team).

---
## Warning
**exorium is currently being rewritten into cogs. This could cause more downtime while it's being rewritten, as well as being able to cause more issues and errors. Of course we will try to keep this to the minimal, for as far as what we can do. But we can not guarantee this will go flawless. If you spot an error/issue or there's something else concerning that you think you need to report, please make an [issue](https://github.com/ThePawKingdom/exorium/issues).**

---
### Commands
All available commands are listed here. This list may not be fully up-to-date at all times.
Please report this in an issue if it's not complete, or make a [pull request](https://github.com/ThePawKingdom/exorium/pulls/) With a complete list. Note that for making a pull request you will need to [fork](https://github.com/ThePawKingdom/exorium/network/members) this repository first, and edit the fork's readme. Prefixes of this bot are `p/` and `exo`

* Syntax args surrounded by `<>` are required. 
* Syntax args surrounded by `()` are optional. 
* Any syntax with `...` means you can give several arguments.
* Crossed through commands are currently not working.

Commands, suggestions or features we still plan to add can be seen in our [TO DO project](https://github.com/ThePawKingdom/exorium/projects/1). If a command doesn't work, please make an [issue](https://github.com/ThePawKingdom/exorium/issues/). Furthermore, if you require support with something within exorium, please join our [support server](https://discord.gg/CEHkNky) and ask for support in it's support channel. 

#### Social Commands
|Command |Syntax                  |
| :----: | :--------------------: |
|hug     |`exo hug <@user>...`    |
|snuggle |`exo snuggle <@user>...`|
|boop    |`exo boop <@user>...`   |
|kiss    |`exo kiss <@user>...`   |
|pat     |`exo pat <@user>...`    |
|cuddle  |`exo cuddle <@user>...` |
|askproto|`exo askexo <arg>...`   |
|bonk    |`exo bonk <@user>...`   |

|Command   |Syntax                   |  
| :------: | :---------------------: |
|lick      |`exo lick <@user>...`    |
|blush     |`exo blush (@user)...`   |
|feed      |`exo feed <@user>...`    |
|glomp     |`exo glomp <@user>...`   |
|happy     |`exo happy (@user)...`   |
|highfive  |`exo highfive <@user>...`|
|wag       |`exo wag (@user)...`     |

#### Moderation Commands
|Command   |Syntax                          |Description                                      |
| :------: | :----------------------------: | :---------------------------------------------: |
|ban       |`exo ban <@user> <@reason>`     |permbans the mentioned user from the guild       | 
|unban     |`exo unban <ID>`                |Unbans the provided user                         |
|softban   |`exo softban <@user> <@reason>` |Bans and immediately unbans the mentioned user   |
|kick      |`exo kick <@user> <@reason>`    |Kicks the mentioned user from the guild          |
|warn      |`exo warn <@user> <@reason>`    |Logs a warn for the mentioned user               |
|delwarn   |`exo delwarn <@user> <@reason>` |Remove a case from someones warning logs         |
|warnings  |`exo warnings <@user>`          |See the mentioned user's logged warnings         |

#### Utility Commands
|Command    |Syntax                         |Description                                       |
| :-------: | :---------------------------: | :----------------------------------------------: |
|serverinfo |`exo serverinfo`               |Shows membercount and guild region                |
|avatar     |`exo avatar <@user>`           |Shows the mentioned user's avatar                 |
|random     |`exo random <arg1> <arg2>...`  |Randomly picks one from the given args            |
|decide     |`exo decide <arg>...`          |Lets people choose with :white_check_mark:	or :x: |
|poll       |`exo poll <arg1>... (arg10)`   |Host a poll with up to 10 things to pick from     |
|say        |`exo say <args>...`            |Repeats what you said in an embed                 |
|id         |`exo id <@user/ID/name>`       |Shows the ID of the provided user                 |

#### Bot-Related Commands
|Command    |Syntax                       |Description                                     |
| :-------: | :-------------------------: | :--------------------------------------------: |
|invite     |`exo invite`                 |Invite exorium through the given invite link    |
|stats      |`exo stats`                  |The statistics of exorium (guilds & total users)|
|links      |`exo links`                  |Links to things related to exorium & TPK        |
|pings      |`exo ping`                   |Shows the bot's latency in seconds              |
|help       |`exo help`                   |Shows all the commands and the exorium team     |
|info       |`exo info <command>`         |Shows information about an individual command   |
|suggest    |`exo suggest <suggestion>`   |Send in a suggestion for exorium                |

---
#### Self Hosting
Selfhosting exorium is not endorsed by the exorium team and is not recommended. We will not provide any type of support for editing or compiling the code in this repository. The source code is given here for education purposes, and so users can better contribute themselves as well as see how the bot works. If you do decide to selfhost exorium, please respect the [license.](https://github.com/ThePawKingdom/exorium/blob/master/LICENSE)
