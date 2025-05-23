CREATE DATABASE IF NOT EXISTS mydb01;
USE mydb01;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);

INSERT INTO user (name, email) VALUES ('zys', 't@hotmail.com');


SET user_1 "{\"id\":1,\"name\":\"zys\",\"email\":\"t@hotmail.com\"}"


CREATE TABLE note (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- 笔记ID（自增主键）
    title VARCHAR(255) NOT NULL,        -- 笔记标题（不能为空）
    content TEXT,                       -- 笔记内容（文本类型）
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 创建时间（默认当前时间）
);

INSERT INTO note (title, content) VALUES ('第一个note', '内容123');

