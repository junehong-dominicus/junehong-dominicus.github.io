# LinkedIn Post Draft — IIoT Edge Devices: Solar Farm Management

Image: `images_for_blog/iiot-edge-devices-solar-farm-management-linkedin.png` (1200×1200)

---

**IIoT Edge Devices — Solar Farm Management**

A solar-plus-storage site has more vendors than people on site. You'll find PV inverters, a met station, trackers, a battery system with its own BMS and power conversion system, enclosure HVAC, a fire and gas panel, and now EV chargers too. Each one exposes its data differently, and most sites are unstaffed.

The EMS needs all of it, on one timeline, plus a safe way to send set-points back.

That's the job of an edge gateway:

→ Read inverters over Modbus TCP/RTU (SunSpec maps): string current, AC power, fault codes
→ Pick up pyranometers and module-temperature sensors on RS-485, or 4–20 mA sensors through a remote I/O module
→ Read battery SoC, SoH, rack temperatures and cell imbalance from the BMS and PCS
→ Monitor and adjust enclosure HVAC over BACnet/IP or MS/TP
→ Act as a local OCPP 1.6J endpoint so charger load shows up next to solar output and battery SoC
→ Give an on-site EMS that has no cloud link a remote dashboard, alerts and history, by polling it as a Modbus TCP server. No EMS rewrite needed.
→ Send it all over mutual-TLS, on its own cellular link so monitoring never touches the owner's network

Once the data is in one place, management gets concrete:

• Output falls below what irradiance and temperature predict → check for soiling, string faults, or clipping
• Cell imbalance grows on one rack → schedule an inspection before it becomes a derate
• A high-power discharge is scheduled → pre-cool the enclosure instead of running HVAC hard afterward
• The fire panel goes into alarm → off-site staff are notified in seconds, with site context
• kWh delivered per charger and metered solar generation → time-stamped, device-attributable data for low-carbon fuel credits and RECs

Three things I've learned from these projects:

1. Put each control function where its response time belongs. Anti-islanding, battery protection and fire shutdown run in milliseconds inside certified equipment. A cellular round trip takes hundreds of milliseconds to seconds, which is fine for dispatch, arbitrage and peak shaving and far too slow for grid protection. The gateway monitors the safety systems and never replaces them.
2. The gateway is not a revenue meter. Credit programs need an approved meter. The gateway's job is to collect cumulative kWh totals from it so the numbers survive a missed reading.
3. Be honest about the interfaces. Modbus, BACnet and OCPP are the easy part. Vendor CAN protocols on some batteries, and utility interfaces like DNP3 or IEEE 2030.5, have to be scoped early, per project.

If you run solar or storage sites, which piece of equipment is still a black box to you?

#IIoT #EdgeComputing #SolarEnergy #EnergyStorage #EVCharging #EMS #RenewableEnergy
