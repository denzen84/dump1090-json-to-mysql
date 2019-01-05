# dump1090-json-to-mysql
Grabs dump1090's 'aircraft.json to SQL database
# SQL TABLE STRUCTURE
## Table "adsb_primary"

```

CREATE TABLE `adsb_primary` (
  `rec_id` bigint(20) NOT NULL,
  `time_unix` double NOT NULL,
  `rssi` float DEFAULT NULL,
  `messages` int(11) NOT NULL DEFAULT '0',
  `seen` float DEFAULT NULL,
  `hex` varchar(16) NOT NULL,
  `flight` varchar(16) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `alt_baro` int(11) DEFAULT NULL,
  `alt_geom` int(11) DEFAULT NULL,
  `gs` float DEFAULT NULL,
  `ias` int(11) DEFAULT NULL,
  `tas` int(11) DEFAULT NULL,
  `mach` float DEFAULT NULL,
  `track` float DEFAULT NULL,
  `track_rate` float DEFAULT NULL,
  `roll` float DEFAULT NULL,
  `mag_heading` float DEFAULT NULL,
  `true_heading` float DEFAULT NULL,
  `baro_rate` int(11) DEFAULT NULL,
  `geom_rate` int(11) DEFAULT NULL,
  `squawk` int(11) DEFAULT NULL,
  `emergency` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `nav_qnh` float DEFAULT NULL,
  `nav_altitude` int(11) DEFAULT NULL,
  `nav_heading` float DEFAULT NULL,
  `nav_modes` varchar(255) DEFAULT NULL,
  `lat` float DEFAULT NULL,
  `lon` float DEFAULT NULL,
  `nic` int(11) DEFAULT NULL,
  `rc` int(11) DEFAULT NULL,
  `seen_pos` float DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  `nic_baro` int(11) DEFAULT NULL,
  `nac_p` int(11) DEFAULT NULL,
  `nac_v` int(11) DEFAULT NULL,
  `sil` int(11) DEFAULT NULL,
  `sil_type` varchar(255) DEFAULT NULL,
  `gva` int(11) DEFAULT NULL,
  `sda` int(11) DEFAULT NULL,
  `mlat` varchar(255) DEFAULT NULL,
  `tisb` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## Indexes for table adsb_primary
```
ALTER TABLE `adsb_primary`
  ADD PRIMARY KEY (`rec_id`),
  ADD KEY `hex` (`hex`),
  ADD KEY `flight` (`flight`),
  ADD KEY `time_unix` (`time_unix`),
  ADD KEY `squawk` (`squawk`);
```

## AUTO_INCREMENT for table `adsb_primary`
```
ALTER TABLE `adsb_primary`
  MODIFY `rec_id` bigint(20) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
```
