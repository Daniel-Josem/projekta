-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 11-04-2025 a las 20:56:16
-- Versión del servidor: 8.0.30
-- Versión de PHP: 8.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_proyectos_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_area`
--

CREATE TABLE `estado_area` (
  `id_estado` int NOT NULL,
  `nombre_estado` varchar(100) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  `estado_cuenta` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `miembros_proyecto`
--

CREATE TABLE `miembros_proyecto` (
  `id_proyecto` int NOT NULL,
  `id_usuario` int NOT NULL,
  `rol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `miembros_proyecto`
--

INSERT INTO `miembros_proyecto` (`id_proyecto`, `id_usuario`, `rol`) VALUES
(1, 3, 'desarrollador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `miembros_proyectos`
--

CREATE TABLE `miembros_proyectos` (
  `id` int NOT NULL,
  `id_usuario` int DEFAULT NULL,
  `id_proyecto` int DEFAULT NULL,
  `rol` enum('administrador','usuario') NOT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  `fecha_fin` datetime DEFAULT NULL,
  `estado_cuenta` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prioridad_tarea`
--

CREATE TABLE `prioridad_tarea` (
  `id_prioridad` int NOT NULL,
  `nombre_prioridad` varchar(100) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  `estado_cuenta` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

CREATE TABLE `proyectos` (
  `id_proyecto` int NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `id_administrador` int DEFAULT NULL,
  `usuario_id` int DEFAULT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  `estado_cuenta` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `proyectos`
--

INSERT INTO `proyectos` (`id_proyecto`, `nombre`, `fecha_inicio`, `fecha_fin`, `id_administrador`, `usuario_id`, `fecha_registro`, `estado_cuenta`) VALUES
(1, 'Desarrollo Web', '2025-04-15', '2025-05-30', NULL, 3, '2025-04-11 15:50:41', 'activo'),
(2, 'PRUEBA', '2025-04-11', '2025-04-12', NULL, NULL, '2025-04-11 15:52:59', 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tareas`
--

CREATE TABLE `tareas` (
  `id_tarea` int NOT NULL,
  `id_proyecto` int DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `id_responsable` int DEFAULT NULL,
  `id_estado` int DEFAULT NULL,
  `id_prioridad` int DEFAULT NULL,
  `id_usuario_asignado` int DEFAULT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  `fecha_fin` datetime DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'pendiente',
  `prioridad` varchar(10) DEFAULT 'media',
  `estado_cuenta` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `tareas`
--

INSERT INTO `tareas` (`id_tarea`, `id_proyecto`, `descripcion`, `fecha_vencimiento`, `id_responsable`, `id_estado`, `id_prioridad`, `id_usuario_asignado`, `fecha_registro`, `fecha_fin`, `estado`, `prioridad`, `estado_cuenta`) VALUES
(1, 1, 'Implementar la página de inicio', '2025-04-22', NULL, NULL, NULL, 3, '2025-04-11 15:50:41', NULL, 'pendiente', 'alta', 'activo'),
(2, 1, 'FIESTA EN LA NOCHE ZUMMMMMBAAAA', '2025-04-11', NULL, NULL, NULL, NULL, '2025-04-11 15:51:36', NULL, 'pendiente', 'media', 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL,
  `nombre_usuario` varchar(100) DEFAULT NULL,
  `correo_electronico` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `contraseña` varchar(255) DEFAULT NULL,
  `rol` varchar(50) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  `fecha_fin` datetime DEFAULT NULL,
  `estado_cuenta` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre_usuario`, `correo_electronico`, `nombre`, `contraseña`, `rol`, `fecha_registro`, `fecha_fin`, `estado_cuenta`) VALUES
(1, 'andesuwu', NULL, NULL, '$2b$12$J1F3yOu.zMAjIBVWQDQBh.ZwE3ooM9ZAHFS8zUc7k/VpDJPVIJ2rm', 'usuario', '2025-04-11 15:46:38', NULL, 'activo'),
(2, 'jose', 'jose@gmail.com', NULL, '$2b$12$ZXZZVZbwM3K.N1/77gCEFuibViARRRF0cYJK6XyTs4JgQOiW3Nbuy', 'lo que sea', '2025-04-11 15:48:49', NULL, 'activo'),
(3, 'juan.perez', 'juan.perez@ejemplo.com', NULL, '$2b$12$aXCXBVxazMMtL4Pz99V4VuU.xkZkOxJQpcP.d7FoFxDViEMKMlvy6', 'administrador', '2025-04-11 15:50:41', NULL, 'activo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estado_area`
--
ALTER TABLE `estado_area`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `miembros_proyecto`
--
ALTER TABLE `miembros_proyecto`
  ADD PRIMARY KEY (`id_proyecto`,`id_usuario`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `miembros_proyectos`
--
ALTER TABLE `miembros_proyectos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `prioridad_tarea`
--
ALTER TABLE `prioridad_tarea`
  ADD PRIMARY KEY (`id_prioridad`);

--
-- Indices de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`id_proyecto`),
  ADD KEY `id_administrador` (`id_administrador`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `tareas`
--
ALTER TABLE `tareas`
  ADD PRIMARY KEY (`id_tarea`),
  ADD KEY `id_proyecto` (`id_proyecto`),
  ADD KEY `id_responsable` (`id_responsable`),
  ADD KEY `id_estado` (`id_estado`),
  ADD KEY `id_prioridad` (`id_prioridad`),
  ADD KEY `id_usuario_asignado` (`id_usuario_asignado`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `nombre_usuario` (`nombre_usuario`),
  ADD UNIQUE KEY `correo` (`correo_electronico`),
  ADD KEY `correo_electronico` (`correo_electronico`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `estado_area`
--
ALTER TABLE `estado_area`
  MODIFY `id_estado` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `miembros_proyectos`
--
ALTER TABLE `miembros_proyectos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `prioridad_tarea`
--
ALTER TABLE `prioridad_tarea`
  MODIFY `id_prioridad` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  MODIFY `id_proyecto` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tareas`
--
ALTER TABLE `tareas`
  MODIFY `id_tarea` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `miembros_proyecto`
--
ALTER TABLE `miembros_proyecto`
  ADD CONSTRAINT `miembros_proyecto_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`),
  ADD CONSTRAINT `miembros_proyecto_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `miembros_proyectos`
--
ALTER TABLE `miembros_proyectos`
  ADD CONSTRAINT `miembros_proyectos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `miembros_proyectos_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`);

--
-- Filtros para la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `proyectos_ibfk_1` FOREIGN KEY (`id_administrador`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `proyectos_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `tareas`
--
ALTER TABLE `tareas`
  ADD CONSTRAINT `tareas_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`),
  ADD CONSTRAINT `tareas_ibfk_2` FOREIGN KEY (`id_responsable`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `tareas_ibfk_3` FOREIGN KEY (`id_estado`) REFERENCES `estado_area` (`id_estado`),
  ADD CONSTRAINT `tareas_ibfk_4` FOREIGN KEY (`id_prioridad`) REFERENCES `prioridad_tarea` (`id_prioridad`),
  ADD CONSTRAINT `tareas_ibfk_5` FOREIGN KEY (`id_usuario_asignado`) REFERENCES `usuarios` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
