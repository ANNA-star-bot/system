-- 路口状态表
CREATE TABLE intersection_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lat REAL,
    lon REAL,
    flow_rate INTEGER,
    truck_rate REAL,
    suggestion TEXT,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 车辆类型统计表
CREATE TABLE vehicle_type_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car INTEGER,
    bus INTEGER,
    truck INTEGER,
    bike INTEGER,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
