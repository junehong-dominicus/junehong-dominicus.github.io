# LinkedIn Post Draft — IIoT Edge AI Devices: Solar Farm Management

Companion article: [IIoT Edge AI Devices: Solar Farm Management](https://junehong-dominicus.github.io/posts/2026-09-26-iiot-edge-devices-solar-farm-management.html)

Image: `images_for_blog/iiot-edge-devices-solar-farm-management-linkedin.png` (1200×1200)

---

**IIoT Edge AI Devices — Solar Farm Management**

A solar-plus-storage site has more vendors than people on site: photovoltaic (PV) inverters, a meteorological (met) station, trackers, a battery system, enclosure HVAC, a fire and gas panel, and now EV chargers. Each exposes its data differently, and most sites are unstaffed.

The energy management system (EMS) needs all of it on one timeline, plus a safe way to send set-points back. That's the job of an edge gateway, the edge device between the field equipment and the dashboard:

→ Read inverters over Modbus TCP/RTU (SunSpec): string current, AC power, faults  
→ Read met sensors on RS-485, or 4–20 mA sensors through a remote I/O module  
→ Read state of charge (SoC), state of health (SoH) and cell imbalance from the battery management system (BMS) and power conversion system (PCS)  
→ Monitor and adjust enclosure HVAC over BACnet  
→ Receive EV charger data as a local Open Charge Point Protocol (OCPP 1.6J) endpoint  
→ Give an on-site EMS with no remote access a dashboard, by polling it over Modbus TCP  
→ Send it all over mutual-TLS to a cloud or on-premise dashboard, via Ethernet, Wi-Fi or its own cellular link  

Once the data is in one place, management gets concrete:

• Output below what irradiance predicts → check soiling, string faults, clipping  
• Cell imbalance grows on one rack → inspect before it becomes a derate  
• High-power discharge scheduled → pre-cool the enclosure  
• Fire panel alarm → off-site staff notified in seconds  

These start as trend rules. Edge AI comes next, once history shows where a fixed threshold stops working: learned baselines for inverter output, and anomaly detection on battery cells before an alarm limit trips.

Carbon credits are the part most owners overlook. EV charging can earn low-carbon fuel credits (California's LCFS, Canada's Clean Fuel Regulations, Germany's GHG quota). Solar can earn RECs, Guarantees of Origin or I-RECs. Every program needs measured, time-stamped energy data traceable to a specific device, which a gateway with its own device certificate can supply. That can turn monitoring into recurring revenue.

Three principles I'm building in from day one:

1. Put control where its response time belongs. Grid and battery protection and fire shutdown run in milliseconds inside certified equipment. A cloud round trip is fine for dispatch and peak shaving, far too slow for protection.
2. The gateway is not a revenue meter. It collects cumulative kWh from an approved meter, so totals survive a missed reading.
3. Be honest about interfaces. Modbus, BACnet and OCPP are easy. Vendor battery CAN protocols and utility interfaces like DNP3 or IEEE 2030.5 need scoping per project.

If you run solar or storage sites, which piece of equipment is still a black box to you?

#IIoT #EdgeComputing #SolarEnergy #EnergyStorage #EVCharging #RenewableEnergy #CarbonCredits
