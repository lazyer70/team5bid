-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-11-28 08:37:04
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `test`
--

-- --------------------------------------------------------

--
-- 資料表結構 `bid`
--

CREATE TABLE `bid` (
  `pid` int(10) NOT NULL,
  `product` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `date` datetime NOT NULL,
  `price` int(10) NOT NULL,
  `act` tinyint(1) NOT NULL,
  `detail` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `bid`
--

INSERT INTO `bid` (`pid`, `product`, `date`, `price`, `act`, `detail`) VALUES
(1, '餅乾', '2022-11-22 15:31:54', 400, 1, '巧克力口味的餅乾'),
(2, '飲料', '2022-11-27 15:33:34', 20, 0, '冰冰涼涼的飲料'),
(3, '衛生紙', '2022-11-26 15:34:23', 30, 0, '就衛生紙'),
(4, '筆', '2022-11-27 15:35:07', 25, 0, '摔到也不會斷水很厲害的筆');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `bid`
--
ALTER TABLE `bid`
  ADD PRIMARY KEY (`pid`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `bid`
--
ALTER TABLE `bid`
  MODIFY `pid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
