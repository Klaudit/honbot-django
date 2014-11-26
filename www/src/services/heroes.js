/* jshint ignore:start */
'use strict';

angular.module('www').factory('heroes',[function(){
    return {"2":{"attacktype":"melee","disp_name":"Armadon","primaryattribute":"Strength","team":"Legion"},"3":{"attacktype":"melee","disp_name":"Behemoth","primaryattribute":"Strength","team":"Legion"},"4":{"attacktype":"melee","disp_name":"Chronos","primaryattribute":"Agility","team":"Hellbourne"},"5":{"attacktype":"ranged","disp_name":"Defiler","primaryattribute":"Intelligence","team":"Hellbourne"},"6":{"attacktype":"melee","disp_name":"Devourer","primaryattribute":"Strength","team":"Hellbourne"},"7":{"attacktype":"melee","disp_name":"Blacksmith","primaryattribute":"Intelligence","team":"Legion"},"8":{"attacktype":"ranged","disp_name":"Slither","primaryattribute":"Agility","team":"Hellbourne"},"9":{"attacktype":"melee","disp_name":"Electrician","primaryattribute":"Strength","team":"Hellbourne"},"10":{"attacktype":"ranged","disp_name":"Nymphora","primaryattribute":"Intelligence","team":"Legion"},"12":{"attacktype":"ranged","disp_name":"Glacius","primaryattribute":"Intelligence","team":"Hellbourne"},"13":{"attacktype":"melee","disp_name":"Hammerstorm","primaryattribute":"Strength","team":"Legion"},"14":{"attacktype":"melee","disp_name":"Night Hound","primaryattribute":"Agility","team":"Legion"},"15":{"attacktype":"melee","disp_name":"Swiftblade","primaryattribute":"Agility","team":"Legion"},"16":{"attacktype":"melee","disp_name":"Blood Hunter","primaryattribute":"Agility","team":"Hellbourne"},"17":{"attacktype":"melee","disp_name":"Kraken","primaryattribute":"Strength","team":"Hellbourne"},"18":{"attacktype":"ranged","disp_name":"Thunderbringer","primaryattribute":"Intelligence","team":"Legion"},"20":{"attacktype":"ranged","disp_name":"Moon Queen","primaryattribute":"Agility","team":"Legion"},"21":{"attacktype":"ranged","disp_name":"Pollywog Priest","primaryattribute":"Intelligence","team":"Legion"},"22":{"attacktype":"melee","disp_name":"Pebbles","primaryattribute":"Strength","team":"Legion"},"24":{"attacktype":"ranged","disp_name":"Soulstealer","primaryattribute":"Agility","team":"Hellbourne"},"25":{"attacktype":"melee","disp_name":"Keeper of the Forest","primaryattribute":"Strength","team":"Legion"},"26":{"attacktype":"melee","disp_name":"The Dark Lady","primaryattribute":"Agility","team":"Hellbourne"},"27":{"attacktype":"ranged","disp_name":"Voodoo Jester","primaryattribute":"Intelligence","team":"Hellbourne"},"29":{"attacktype":"melee","disp_name":"War Beast","primaryattribute":"Strength","team":"Hellbourne"},"30":{"attacktype":"ranged","disp_name":"Wildsoul","primaryattribute":"Agility","team":"Legion"},"31":{"attacktype":"melee","disp_name":"Zephyr","primaryattribute":"Agility","team":"Legion"},"34":{"attacktype":"melee","disp_name":"Pharaoh","primaryattribute":"Strength","team":"Hellbourne"},"35":{"attacktype":"ranged","disp_name":"Tempest","primaryattribute":"Intelligence","team":"Legion"},"36":{"attacktype":"ranged","disp_name":"Ophelia","primaryattribute":"Intelligence","team":"Legion"},"37":{"attacktype":"melee","disp_name":"Magebane","primaryattribute":"Agility","team":"Legion"},"38":{"attacktype":"melee","disp_name":"Legionnaire","primaryattribute":"Strength","team":"Legion"},"39":{"attacktype":"melee","disp_name":"Predator","primaryattribute":"Strength","team":"Legion"},"40":{"attacktype":"melee","disp_name":"Accursed","primaryattribute":"Strength","team":"Hellbourne"},"41":{"attacktype":"melee","disp_name":"Nomad","primaryattribute":"Agility","team":"Legion"},"42":{"attacktype":"melee","disp_name":"The Madman","primaryattribute":"Agility","team":"Hellbourne"},"43":{"attacktype":"ranged","disp_name":"Demented Shaman","primaryattribute":"Intelligence","team":"Hellbourne"},"44":{"attacktype":"melee","disp_name":"Scout","primaryattribute":"Agility","team":"Legion"},"89":{"attacktype":"melee","disp_name":"Jeraziah","primaryattribute":"Strength","team":"Legion"},"90":{"attacktype":"ranged","disp_name":"Torturer","primaryattribute":"Intelligence","team":"Hellbourne"},"91":{"attacktype":"ranged","disp_name":"Puppet Master","primaryattribute":"Intelligence","team":"Hellbourne"},"92":{"attacktype":"ranged","disp_name":"Arachna","primaryattribute":"Agility","team":"Hellbourne"},"93":{"attacktype":"ranged","disp_name":"Hellbringer","primaryattribute":"Intelligence","team":"Hellbourne"},"94":{"attacktype":"ranged","disp_name":"Pyromancer","primaryattribute":"Intelligence","team":"Legion"},"95":{"attacktype":"melee","disp_name":"Pestilence","primaryattribute":"Strength","team":"Hellbourne"},"96":{"attacktype":"melee","disp_name":"Maliken","primaryattribute":"Strength","team":"Hellbourne"},"102":{"attacktype":"ranged","disp_name":"Andromeda","primaryattribute":"Agility","team":"Legion"},"103":{"attacktype":"ranged","disp_name":"Valkyrie","primaryattribute":"Agility","team":"Legion"},"104":{"attacktype":"ranged","disp_name":"Wretched Hag","primaryattribute":"Intelligence","team":"Hellbourne"},"105":{"attacktype":"ranged","disp_name":"Succubus","primaryattribute":"Intelligence","team":"Hellbourne"},"106":{"attacktype":"melee","disp_name":"Magmus","primaryattribute":"Strength","team":"Hellbourne"},"108":{"attacktype":"ranged","disp_name":"Plague Rider","primaryattribute":"Intelligence","team":"Hellbourne"},"109":{"attacktype":"ranged","disp_name":"Soul Reaper","primaryattribute":"Intelligence","team":"Hellbourne"},"110":{"attacktype":"melee","disp_name":"Pandamonium","primaryattribute":"Strength","team":"Legion"},"114":{"attacktype":"ranged","disp_name":"Corrupted Disciple","primaryattribute":"Agility","team":"Hellbourne"},"115":{"attacktype":"ranged","disp_name":"Vindicator","primaryattribute":"Intelligence","team":"Legion"},"116":{"attacktype":"melee","disp_name":"Sand Wraith","primaryattribute":"Agility","team":"Hellbourne"},"117":{"attacktype":"melee","disp_name":"Rampage","primaryattribute":"Strength","team":"Legion"},"120":{"attacktype":"ranged","disp_name":"Witch Slayer","primaryattribute":"Intelligence","team":"Legion"},"121":{"attacktype":"ranged","disp_name":"Forsaken Archer","primaryattribute":"Agility","team":"Hellbourne"},"122":{"attacktype":"ranged","disp_name":"Engineer","primaryattribute":"Agility","team":"Legion"},"123":{"attacktype":"melee","disp_name":"Deadwood","primaryattribute":"Strength","team":"Hellbourne"},"124":{"attacktype":"ranged","disp_name":"The Chipper","primaryattribute":"Intelligence","team":"Legion"},"125":{"attacktype":"ranged","disp_name":"Bubbles","primaryattribute":"Intelligence","team":"Legion"},"126":{"attacktype":"melee","disp_name":"Fayde","primaryattribute":"Agility","team":"Hellbourne"},"127":{"attacktype":"melee","disp_name":"Balphagore","primaryattribute":"Strength","team":"Hellbourne"},"128":{"attacktype":"melee","disp_name":"Gauntlet","primaryattribute":"Strength","team":"Hellbourne"},"160":{"attacktype":"melee","disp_name":"Tundra","primaryattribute":"Strength","team":"Legion"},"161":{"attacktype":"melee","disp_name":"The Gladiator","primaryattribute":"Strength","team":"Legion"},"162":{"attacktype":"ranged","disp_name":"Doctor Repulsor","primaryattribute":"Intelligence","team":"Hellbourne"},"163":{"attacktype":"ranged","disp_name":"Flint Beastwood","primaryattribute":"Agility","team":"Hellbourne"},"164":{"attacktype":"ranged","disp_name":"Bombardier","primaryattribute":"Intelligence","team":"Legion"},"165":{"attacktype":"melee","disp_name":"Moraxus","primaryattribute":"Strength","team":"Hellbourne"},"166":{"attacktype":"ranged","disp_name":"Myrmidon","primaryattribute":"Intelligence","team":"Hellbourne"},"167":{"attacktype":"melee","disp_name":"Dampeer","primaryattribute":"Agility","team":"Hellbourne"},"168":{"attacktype":"ranged","disp_name":"Empath","primaryattribute":"Intelligence","team":"Legion"},"169":{"attacktype":"ranged","disp_name":"Aluna","primaryattribute":"Intelligence","team":"Legion"},"170":{"attacktype":"melee","disp_name":"Tremble","primaryattribute":"Agility","team":"Hellbourne"},"185":{"attacktype":"ranged","disp_name":"Silhouette","primaryattribute":"Agility","team":"Legion"},"187":{"attacktype":"ranged","disp_name":"Flux","primaryattribute":"Strength","team":"Legion"},"188":{"attacktype":"ranged","disp_name":"Martyr","primaryattribute":"Intelligence","team":"Legion"},"192":{"attacktype":"melee","disp_name":" \t\tAmun-Ra","primaryattribute":"Strength","team":"Hellbourne"},"194":{"attacktype":"melee","disp_name":"Parasite","primaryattribute":"Intelligence","team":"Hellbourne"},"195":{"attacktype":"ranged","disp_name":"Emerald Warden","primaryattribute":"Agility","team":"Legion"},"196":{"attacktype":"ranged","disp_name":"Revenant","primaryattribute":"Intelligence","team":"Hellbourne"},"197":{"attacktype":"melee","disp_name":"Monkey King","primaryattribute":"Agility","team":"Legion"},"201":{"attacktype":"melee","disp_name":"Drunken Master","primaryattribute":"Strength","team":"Legion"},"202":{"attacktype":"ranged","disp_name":"Master Of Arms","primaryattribute":"Agility","team":"Legion"},"203":{"attacktype":"ranged","disp_name":"Rhapsody","primaryattribute":"Intelligence","team":"Legion"},"204":{"attacktype":"melee","disp_name":"Geomancer","primaryattribute":"Intelligence","team":"Hellbourne"},"205":{"attacktype":"ranged","disp_name":"Midas","primaryattribute":"Strength","team":"Legion"},"206":{"attacktype":"melee","disp_name":"Cthulhuphant","primaryattribute":"Strength","team":"Hellbourne"},"207":{"attacktype":"ranged","disp_name":"Monarch","primaryattribute":"Intelligence","team":"Legion"},"208":{"attacktype":"melee","disp_name":"Gemini","primaryattribute":"Agility","team":"Hellbourne"},"209":{"attacktype":"melee","disp_name":"Lord Salforis","primaryattribute":"Strength","team":"Hellbourne"},"210":{"attacktype":"melee","disp_name":"Shadowblade","primaryattribute":"Agility","team":"Hellbourne"},"211":{"attacktype":"ranged","disp_name":"Artesia","primaryattribute":"Intelligence","team":"Hellbourne"},"212":{"attacktype":"ranged","disp_name":"Gravekeeper","primaryattribute":"Intelligence","team":"Hellbourne"},"213":{"attacktype":"melee","disp_name":"Berzerker","primaryattribute":"Strength","team":"Legion"},"214":{"attacktype":"ranged","disp_name":"Draconis","primaryattribute":"Agility","team":"Legion"},"215":{"attacktype":"ranged","disp_name":"Kinesis","primaryattribute":"Intelligence","team":"Legion"},"216":{"attacktype":"ranged","disp_name":"Gunblade","primaryattribute":"Agility","team":"Hellbourne"},"217":{"attacktype":"ranged","disp_name":"Blitz","primaryattribute":"Agility","team":"Legion"},"218":{"attacktype":"ranged","disp_name":"Artillery","primaryattribute":"Agility","team":"Legion"},"219":{"attacktype":"ranged","disp_name":"Ellonia","primaryattribute":"Intelligence","team":"Legion"},"220":{"attacktype":"ranged","disp_name":"Riftwalker","primaryattribute":"Intelligence","team":"Hellbourne"},"221":{"attacktype":"melee","disp_name":"Bramble","primaryattribute":"Strength","team":"Legion"},"222":{"attacktype":"melee","disp_name":"Ravenor","primaryattribute":"Strength","team":"Hellbourne"},"223":{"attacktype":"ranged","disp_name":"Prophet","primaryattribute":"Intelligence","team":"Hellbourne"},"224":{"attacktype":"melee","disp_name":"Rally","primaryattribute":"Strength","team":"Legion"},"225":{"attacktype":"melee","disp_name":"Oogie","primaryattribute":"Intelligence","team":"Legion"},"226":{"attacktype":"melee","disp_name":"Solstice","primaryattribute":"Strength","team":"Legion"},"227":{"attacktype":"ranged","disp_name":"Pearl","primaryattribute":"Intelligence","team":"Legion"},"228":{"attacktype":"melee","disp_name":"Grinex","primaryattribute":"Agility","team":"Hellbourne"},"229":{"attacktype":"melee","disp_name":"Lodestone","primaryattribute":"Strength","team":"Hellbourne"},"230":{"attacktype":"ranged","disp_name":"Bushwack","primaryattribute":"Agility","team":"Hellbourne"},"232":{"attacktype":"melee","disp_name":"Salomon","primaryattribute":"Strength","team":"Legion"},"233":{"attacktype":"melee","disp_name":"Prisoner 945","primaryattribute":"Strength","team":"Legion"},"234":{"attacktype":"melee","disp_name":"Sir Benzington","primaryattribute":"Agility","team":"Legion"},"235":{"attacktype":"ranged","disp_name":"Circe","primaryattribute":"Intelligence","team":"Hellbourne"},"236":{"attacktype":"ranged","disp_name":"Klanx","primaryattribute":"Agility","team":"Hellbourne"},"237":{"attacktype":"melee","disp_name":"Riptide","primaryattribute":"Strength","team":"Hellbourne"},"238":{"attacktype":"ranged","disp_name":"Moira","primaryattribute":"Agility","team":"Legion"},"240":{"attacktype":"ranged","disp_name":"Tarot","primaryattribute":"Agility","team":"Legion"},"241":{"attacktype":"melee","disp_name":"Kane","primaryattribute":"Strength","team":"Hellbourne"}};
}]);

/* jshint ignore:end */