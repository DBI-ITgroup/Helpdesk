-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2025 at 11:24 AM
-- Server version: 11.8.1-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `helpdeskapp1`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(2, 'Administrator'),
(5, 'CAB'),
(1, 'End-User'),
(3, 'L1_Technician'),
(4, 'L2_Technician');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(2, 3, 29),
(3, 4, 31);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add ticket', 7, 'add_ticket'),
(26, 'Can change ticket', 7, 'change_ticket'),
(27, 'Can delete ticket', 7, 'delete_ticket'),
(28, 'Can view ticket', 7, 'view_ticket'),
(29, 'Can view pending tickets', 7, 'view_pending_tickets'),
(30, 'Can view completed tickets', 7, 'view_completed_tickets'),
(31, 'Can view escalated tickets', 7, 'view_escalated_tickets');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-03-28 12:18:20.785694', '3', 'Tester 2 (L1_Technician)', 1, '[{\"added\": {}}]', 6, 2),
(2, '2025-03-28 12:18:54.474505', '3', 'Tester 2 (L1_Technician)', 2, '[]', 6, 2),
(3, '2025-03-28 12:21:57.433084', '4', 'Tester 3 (L1_Technician)', 1, '[{\"added\": {}}]', 6, 2),
(4, '2025-03-28 12:23:59.082708', '5', 'Tester 4 (L2_Technician)', 1, '[{\"added\": {}}]', 6, 2),
(5, '2025-03-28 12:24:43.036488', '5', 'Tester 4 (L2_Technician)', 2, '[]', 6, 2),
(6, '2025-03-29 17:31:07.410186', '3', 'Tester 2 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(7, '2025-03-29 17:38:56.392992', '1', 'End-User', 1, '[{\"added\": {}}]', 3, 2),
(8, '2025-03-29 17:39:33.444999', '2', 'Administrator', 1, '[{\"added\": {}}]', 3, 2),
(9, '2025-03-29 17:39:58.569504', '3', 'L1_Technician', 1, '[{\"added\": {}}]', 3, 2),
(10, '2025-03-29 17:40:18.247730', '4', 'L2_Technician', 1, '[{\"added\": {}}]', 3, 2),
(11, '2025-03-29 17:40:37.248325', '5', 'CAB', 1, '[{\"added\": {}}]', 3, 2),
(12, '2025-03-29 17:41:09.482641', '3', 'Tester 2 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 6, 2),
(13, '2025-03-29 17:47:53.858087', '3', 'L1_Technician', 2, '[]', 3, 2),
(14, '2025-03-29 18:06:30.441244', '3', 'Tester 2 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(15, '2025-03-29 18:07:32.141094', '3', 'Tester 2 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(16, '2025-03-29 18:32:22.373764', '3', 'Tester 2 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(17, '2025-03-29 18:33:18.583404', '4', 'Tester 3 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(18, '2025-03-29 18:36:05.182731', '3', 'L1_Technician', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 2),
(19, '2025-03-29 18:48:31.881671', '3', 'Tester 2 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(20, '2025-03-29 18:49:15.971275', '3', 'L1_Technician', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 2),
(21, '2025-03-29 18:50:19.630088', '4', 'Tester 3 (L1_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(22, '2025-03-29 18:51:24.471379', '3', 'L1_Technician', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 2),
(23, '2025-03-29 20:20:18.030013', '5', 'Tester 4 (L2_Technician)', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 2),
(24, '2025-03-31 07:14:49.449672', '4', 'L2_Technician', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 2),
(25, '2025-03-31 07:37:46.464111', '6', 'Tester 5 (L2_Technician)', 1, '[{\"added\": {}}]', 6, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'helpdeskapp', 'customuser'),
(7, 'helpdeskapp', 'ticket'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-03-28 12:07:48.203270'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-03-28 12:07:48.283820'),
(3, 'auth', '0001_initial', '2025-03-28 12:07:48.637410'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-03-28 12:07:48.712287'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-03-28 12:07:48.720639'),
(6, 'auth', '0004_alter_user_username_opts', '2025-03-28 12:07:48.730099'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-03-28 12:07:48.740787'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-03-28 12:07:48.745781'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-03-28 12:07:48.755968'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-03-28 12:07:48.766225'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-03-28 12:07:48.775631'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-03-28 12:07:48.830832'),
(13, 'auth', '0011_update_proxy_permissions', '2025-03-28 12:07:48.842283'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-03-28 12:07:48.850982'),
(15, 'helpdeskapp', '0001_initial', '2025-03-28 12:07:49.374116'),
(16, 'admin', '0001_initial', '2025-03-28 12:07:49.522449'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-03-28 12:07:49.533783'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-03-28 12:07:49.551122'),
(19, 'helpdeskapp', '0002_alter_ticket_options_alter_customuser_role', '2025-03-28 12:07:49.570147'),
(20, 'helpdeskapp', '0003_ticket_assigned_technician', '2025-03-28 12:07:49.678458'),
(21, 'helpdeskapp', '0004_alter_ticket_status', '2025-03-28 12:07:49.696248'),
(22, 'helpdeskapp', '0005_rename_ticket_id_ticket_id', '2025-03-28 12:07:49.760652'),
(23, 'sessions', '0001_initial', '2025-03-28 12:07:49.833980'),
(24, 'helpdeskapp', '0006_alter_ticket_options_alter_ticket_status', '2025-03-29 20:18:35.136932');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('nqhjlxov8kpbwjiiqnotmjm4lkjvm0qr', '.eJxVjMsOwiAUBf-FtSFgeenSfb-B3AdI1UBS2pXx322TLnR7Zua8RYR1KXHtaY4Ti6sw4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uXYOL1uh_t3UKCXrbZg_MWjJuIzuhQUQlaKNBl0A-bMqLUNDgJlowePAdEm0A6JXdig-HwBByg5DA:1tzBKm:69GATC5rynTyMzp581G7_i3idRcPbUBN4cPpR0hlDd4', '2025-04-14 09:21:32.814735');

-- --------------------------------------------------------

--
-- Table structure for table `helpdeskapp_customuser`
--

CREATE TABLE `helpdeskapp_customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `helpdeskapp_customuser`
--

INSERT INTO `helpdeskapp_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `full_name`, `email`, `role`) VALUES
(1, 'pbkdf2_sha256$870000$IJFxN89JYdjosXROIWTXWe$lAHvyeEQdrI50SQdV/SoQTX5KnCddDSnNYtTPRRJAAs=', '2025-03-31 09:20:32.113451', 0, 'tester1@gmail.com', '', '', 0, 1, '2025-03-28 12:09:33.389074', 'Tester 1', 'tester1@gmail.com', 'End-User'),
(2, 'pbkdf2_sha256$870000$Roi4GmnbM1PDpJigbudkzG$PJTla1at4zXE0vQ3cgV648iB46llRc6lsSwzXrWU948=', '2025-03-31 08:48:37.697128', 1, 'sinelizwigebeda@gmail.com', '', '', 1, 1, '2025-03-28 12:14:39.208753', 'Sinelizwi Gebeda', 'sinelizwigebeda@gmail.com', 'Administrator'),
(3, 'pbkdf2_sha256$870000$g4QHwZwZ5jqrdZ48CcGk4d$AjilK+ppLO/v/IGoA0QadcTeHMV3gNLsMAznbdYqkqk=', '2025-03-31 09:21:19.483259', 0, 'tester2@gmail.com', '', '', 0, 1, '2025-03-28 12:18:19.000000', 'Tester 2', 'tester2@gmail.com', 'L1_Technician'),
(4, 'pbkdf2_sha256$870000$CW1xDY27M4pUX7SDvwrSZR$dKs9P/O8FKCnXVR5MXQPspwvFpOdZhzPlpaMBfj4/x8=', '2025-03-31 09:21:32.809692', 0, 'tester3@gmail.com', '', '', 0, 1, '2025-03-28 12:21:56.000000', 'Tester 3', 'tester3@gmail.com', 'L1_Technician'),
(5, 'pbkdf2_sha256$870000$3zz5AvngCTgyVkiBrM4Y9G$8qAHPa/5dLQM8qOALUTihElPY/lZt9JeeV2qL+0fbJ8=', '2025-03-31 09:18:37.205168', 0, 'tester4@gmail.com', '', '', 0, 1, '2025-03-28 12:23:58.000000', 'Tester 4', 'tester4@gmail.com', 'L2_Technician'),
(6, 'pbkdf2_sha256$870000$xSQT9RuLDT9nRnxACnOGFr$76dyR/a2Vi5+CQje2GO4FqPqj92bfQKL/ahOy8cg74o=', '2025-03-31 09:17:20.118813', 0, 'tester5@gmail.com', '', '', 0, 1, '2025-03-31 07:37:45.733254', 'Tester 5', 'tester5@gmail.com', 'L2_Technician');

-- --------------------------------------------------------

--
-- Table structure for table `helpdeskapp_customuser_groups`
--

CREATE TABLE `helpdeskapp_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `helpdeskapp_customuser_groups`
--

INSERT INTO `helpdeskapp_customuser_groups` (`id`, `customuser_id`, `group_id`) VALUES
(1, 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `helpdeskapp_customuser_user_permissions`
--

CREATE TABLE `helpdeskapp_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `helpdeskapp_customuser_user_permissions`
--

INSERT INTO `helpdeskapp_customuser_user_permissions` (`id`, `customuser_id`, `permission_id`) VALUES
(6, 4, 29),
(7, 5, 31),
(8, 6, 31);

-- --------------------------------------------------------

--
-- Table structure for table `helpdeskapp_ticket`
--

CREATE TABLE `helpdeskapp_ticket` (
  `id` int(11) NOT NULL,
  `ticket_number` varchar(20) NOT NULL,
  `ticket_title` varchar(255) NOT NULL,
  `department` varchar(100) NOT NULL,
  `contact_info` varchar(255) NOT NULL,
  `problem_description` longtext NOT NULL,
  `priority_level` varchar(50) NOT NULL,
  `preferred_contact_method` varchar(50) NOT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `date_created_on` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `assigned_technician_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `helpdeskapp_ticket`
--

INSERT INTO `helpdeskapp_ticket` (`id`, `ticket_number`, `ticket_title`, `department`, `contact_info`, `problem_description`, `priority_level`, `preferred_contact_method`, `attachment`, `date_created_on`, `status`, `user_id`, `assigned_technician_id`) VALUES
(1, '2C06D47A', 'Testing 1', 'IT', '0111111111', 'h,mnbhvgfch,./,m', 'Medium', 'Email', 'attachments/3d_pie_chart_LwAd7Y2.jpg', '2025-03-28 12:10:07.233057', 'Pending', 1, NULL),
(2, 'B9D80C95', 'Testing 2', 'IT', '0111111111', 'hgfdsfgh,.m nbvcxzdfg,.mnb mhgfddgh\'hgf  nhgfxcghv,./mnbvcxdfjm, rgh,mnbvcfdr.,mn dfgh,.mnbvcdswernmbvcxzdr4hgfdserr432134m,nbvcdfghhn,mbvcfgh.,mnbvcxdfghbnm, dfghmnbhgfre21234hgfdfxcgvbnm,. dfghhgfdghmnbvcfdgh.,mhgfre2134ghchvnbm,.nb', 'High', 'Email', '', '2025-03-28 12:26:53.585698', 'Escalated', 1, 5),
(3, '93771961', 'Testing 3', 'HR', '0111111111', 'nbvcxvbnm,. nmhgfrgh.m,nbvfdxcv ,hgfdsfghhgfdswerumnb sdgfhm,nbvcfdrghmnbvcxdsfghm,n dsfghmnbvcdfxsfghm,nbvcfdswermnbvcfvbnm   dfghre21234432werfghm,nb nbvcdfghnmbvcdfghhgfrewq23w4', 'Medium', 'Email', 'attachments/3d_pie_chart_NtAUy54.jpg', '2025-03-28 12:28:11.314382', 'In Progress', 1, 4),
(4, '0D88E276', 'Testing 4', 'Finance', '0111111111', 'hgn.bhhgfcvb nm,.mn', 'Low', 'Phone', '', '2025-03-31 08:25:25.751964', 'Escalated', 1, 3),
(5, 'B16B4473', 'Testing 5', 'IT', '0111111111', 'gh,.m nbh', 'Medium', 'Phone', 'attachments/3d_pie_chart_ixbxtz3.jpg', '2025-03-31 09:14:28.844590', 'Pending', 1, 3),
(6, 'AFDF6D74', 'Testing 6', 'HR', '0111111111', 'rdfghhbvbnm', 'Low', 'Phone', 'attachments/mail.png', '2025-03-31 09:21:07.124251', 'Pending', 1, 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_helpdeskapp_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `helpdeskapp_customuser`
--
ALTER TABLE `helpdeskapp_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `helpdeskapp_customuser_groups`
--
ALTER TABLE `helpdeskapp_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `helpdeskapp_customuser_g_customuser_id_group_id_a8125761_uniq` (`customuser_id`,`group_id`),
  ADD KEY `helpdeskapp_customuser_groups_group_id_2756f86f_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `helpdeskapp_customuser_user_permissions`
--
ALTER TABLE `helpdeskapp_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `helpdeskapp_customuser_u_customuser_id_permission_8c04e82e_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `helpdeskapp_customus_permission_id_87bb2b51_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `helpdeskapp_ticket`
--
ALTER TABLE `helpdeskapp_ticket`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ticket_number` (`ticket_number`),
  ADD KEY `helpdeskapp_ticket_user_id_3cda6bea_fk_helpdeskapp_customuser_id` (`user_id`),
  ADD KEY `helpdeskapp_ticket_assigned_technician__73f081b1_fk_helpdeska` (`assigned_technician_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `helpdeskapp_customuser`
--
ALTER TABLE `helpdeskapp_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `helpdeskapp_customuser_groups`
--
ALTER TABLE `helpdeskapp_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `helpdeskapp_customuser_user_permissions`
--
ALTER TABLE `helpdeskapp_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `helpdeskapp_ticket`
--
ALTER TABLE `helpdeskapp_ticket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_helpdeskapp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `helpdeskapp_customuser` (`id`);

--
-- Constraints for table `helpdeskapp_customuser_groups`
--
ALTER TABLE `helpdeskapp_customuser_groups`
  ADD CONSTRAINT `helpdeskapp_customus_customuser_id_705e4c89_fk_helpdeska` FOREIGN KEY (`customuser_id`) REFERENCES `helpdeskapp_customuser` (`id`),
  ADD CONSTRAINT `helpdeskapp_customuser_groups_group_id_2756f86f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `helpdeskapp_customuser_user_permissions`
--
ALTER TABLE `helpdeskapp_customuser_user_permissions`
  ADD CONSTRAINT `helpdeskapp_customus_customuser_id_04171ffd_fk_helpdeska` FOREIGN KEY (`customuser_id`) REFERENCES `helpdeskapp_customuser` (`id`),
  ADD CONSTRAINT `helpdeskapp_customus_permission_id_87bb2b51_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `helpdeskapp_ticket`
--
ALTER TABLE `helpdeskapp_ticket`
  ADD CONSTRAINT `helpdeskapp_ticket_assigned_technician__73f081b1_fk_helpdeska` FOREIGN KEY (`assigned_technician_id`) REFERENCES `helpdeskapp_customuser` (`id`),
  ADD CONSTRAINT `helpdeskapp_ticket_user_id_3cda6bea_fk_helpdeskapp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `helpdeskapp_customuser` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
