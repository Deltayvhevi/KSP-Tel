//Raw Telemetry log
//Made By Delta
//Version 1.0
//Variables

//Main Script Body 

    wait until ag1.
    until ag10 {
        clearScreen.
        print("Nominal Logging").

        log (round(missionTime) + ": " + "GroundSpeed: " + round(ship:groundSpeed)) to GroundVelocityLog.txt.
        log (round(missionTime) + ": " + "TotalVelocity: " + round(ship:verticalspeed + ship:groundspeed)) to VelocityLog.txt.
        log (round(missionTime) + ": " + "VerticalSpeed: " + round(ship:verticalspeed)) to VerticalVelocityLog.txt.
        log (round(missionTime) + ": " + "Thrust: " + round(ship:availablethrust)) to ThrustLog.txt.
        log (round(missionTime) + ": " + "Altitude: " + round(ship:altitude)) to AltitudeLog.txt.
        log (round(missionTime) + ": " + "ShipParts: " + ship:Parts:length) to ShipPartsLog.txt.
        log (round(missionTime) + ": " + "Apogee: " + round(ship:apoapsis)) to ApogeeLog.txt.
        log (round(missionTime) + ": " + "Perigee: " + round(ship:periapsis)) to PerigeeLog.txt.
        log (round(missionTime) + ": " + "RadarAltitude: " + round(alt:radar)) to RadarAltitudeLog.txt.

        wait 3.
    }