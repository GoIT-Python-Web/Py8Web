--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Debian 14.2-1.pgdg110+1)
-- Dumped by pg_dump version 14.2

-- Started on 2023-02-17 19:37:22

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3356 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16384)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16425)
-- Name: contact_persons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contact_persons (
    id integer NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(150) NOT NULL,
    cell_phone character varying(150) NOT NULL,
    address character varying(150),
    student_id integer NOT NULL
);


ALTER TABLE public.contact_persons OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16424)
-- Name: contact_persons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contact_persons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contact_persons_id_seq OWNER TO postgres;

--
-- TOC entry 3357 (class 0 OID 0)
-- Dependencies: 216
-- Name: contact_persons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contact_persons_id_seq OWNED BY public.contact_persons.id;


--
-- TOC entry 211 (class 1259 OID 16390)
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    id integer NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(150) NOT NULL,
    cell_phone character varying(150) NOT NULL,
    address character varying(150)
);


ALTER TABLE public.students OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16389)
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO postgres;

--
-- TOC entry 3358 (class 0 OID 0)
-- Dependencies: 210
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- TOC entry 213 (class 1259 OID 16399)
-- Name: teachers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teachers (
    id integer NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(150) NOT NULL,
    cell_phone character varying(150) NOT NULL,
    address character varying(150),
    start_work date,
    created_at timestamp without time zone
);


ALTER TABLE public.teachers OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16398)
-- Name: teachers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teachers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teachers_id_seq OWNER TO postgres;

--
-- TOC entry 3359 (class 0 OID 0)
-- Dependencies: 212
-- Name: teachers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teachers_id_seq OWNED BY public.teachers.id;


--
-- TOC entry 215 (class 1259 OID 16408)
-- Name: teachers_to_students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teachers_to_students (
    id integer NOT NULL,
    teacher_id integer,
    student_id integer
);


ALTER TABLE public.teachers_to_students OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16407)
-- Name: teachers_to_students_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teachers_to_students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teachers_to_students_id_seq OWNER TO postgres;

--
-- TOC entry 3360 (class 0 OID 0)
-- Dependencies: 214
-- Name: teachers_to_students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teachers_to_students_id_seq OWNED BY public.teachers_to_students.id;


--
-- TOC entry 3189 (class 2604 OID 16428)
-- Name: contact_persons id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_persons ALTER COLUMN id SET DEFAULT nextval('public.contact_persons_id_seq'::regclass);


--
-- TOC entry 3186 (class 2604 OID 16393)
-- Name: students id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- TOC entry 3187 (class 2604 OID 16402)
-- Name: teachers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers ALTER COLUMN id SET DEFAULT nextval('public.teachers_id_seq'::regclass);


--
-- TOC entry 3188 (class 2604 OID 16411)
-- Name: teachers_to_students id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers_to_students ALTER COLUMN id SET DEFAULT nextval('public.teachers_to_students_id_seq'::regclass);


--
-- TOC entry 3342 (class 0 OID 16384)
-- Dependencies: 209
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alembic_version VALUES ('568e9ad25eb8');


--
-- TOC entry 3350 (class 0 OID 16425)
-- Dependencies: 217
-- Data for Name: contact_persons; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.contact_persons VALUES (1, 'Соломія', 'Баранник', 'mhaidabura@gov.ua', '+38 (074) 980-75-11', 'шосе Володимира Вінниченка, буд. 8 кв. 3, Бунге , 32392', 6);
INSERT INTO public.contact_persons VALUES (2, 'Костянтин', 'Лубенець', 'danchukoksana@i.ua', '971-09-30', 'провулок Маланова, буд. 37, Васильків, 59700', 8);
INSERT INTO public.contact_persons VALUES (3, 'Мілена', 'Штокало', 'rudykmaksym@ukr.net', '888-48-10', 'набережна Сирітський, буд. 15, Павлоград, 30846', 5);
INSERT INTO public.contact_persons VALUES (4, 'Ярема', 'Якимчук', 'andriienkomykhailyna@gmail.com', '283-37-02', 'шосе 4-та Суворовська, буд. 912 кв. 04, Яремче, 98356', 6);
INSERT INTO public.contact_persons VALUES (5, 'Олена', 'Гаврюшенко', 'symoniemets@gmail.com', '+38 (002) 263-00-85', 'шосе Сортувальна 1-ша, буд. 4, Молодогвардійськ, 32497', 10);
INSERT INTO public.contact_persons VALUES (6, 'Опанас', 'Цюпа', 'taras35@gmail.com', '+38 (009) 248-98-45', 'парк Петра Лещенка, буд. 039 кв. 465, Кадіївка, 46173', 2);
INSERT INTO public.contact_persons VALUES (7, 'Зиновій', 'Зарудний', 'mykolai41@gmail.com', '719-34-04', 'сквер Травневий 3-й, буд. 8, Лебедин, 78629', 2);
INSERT INTO public.contact_persons VALUES (8, 'Віктор', 'Артюшенко', 'lishchak@ukr.net', '+38 063 011-86-98', 'парк Композитора Глинки, буд. 549, Хрустальний, 13570', 1);
INSERT INTO public.contact_persons VALUES (9, 'Гліб', 'Оробець', 'cvovk@gmail.com', '101-44-03', 'вулиця Мічуріна, буд. 9 кв. 49, Мар''їнка, 72577', 5);
INSERT INTO public.contact_persons VALUES (10, 'Емілія', 'Малишко', 'pylypchalenko@gmail.com', '005 541-92-70', 'провулок Східчастий, буд. 232, Любомль, 13654', 2);
INSERT INTO public.contact_persons VALUES (11, 'Макар', 'Нестеренко', 'dmytrokaras@ukr.net', '+38 038 255-84-48', 'проспект 8-ма Суворовська, буд. 37, Сокаль, 53941', 4);
INSERT INTO public.contact_persons VALUES (12, 'Анжела', 'Адамчук', 'tymofiiturkalo@gmail.com', '157 82 42', 'узвіз Баштанна, буд. 2 кв. 2, Пологи , 65057', 9);
INSERT INTO public.contact_persons VALUES (13, 'Софія', 'Канівець', 'chuprynaedyta@meta.ua', '+38 070 895-18-41', 'шосе Андреєвського, буд. 32 кв. 3, Хирів, 68273', 8);
INSERT INTO public.contact_persons VALUES (14, 'Михайлина', 'Щербань', 'iosyp90@i.ua', '405 13 32', 'проспект Вознесенський, буд. 24, Моршин, 57960', 10);
INSERT INTO public.contact_persons VALUES (15, 'Артем', 'Зінченко', 'iosyp48@ukr.net', '018 422 86 63', 'вулиця Новомосковська дорога, буд. 780, Мала Виска, 48730', 5);


--
-- TOC entry 3344 (class 0 OID 16390)
-- Dependencies: 211
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.students VALUES (1, 'Ірена', 'Гайдамака', 'mykytaokhrimenko@email.ua', '+38 094 718-12-26', 'сквер Романтиків, буд. 756, Городня, 39411');
INSERT INTO public.students VALUES (2, 'Амалія', 'Товстуха', 'anton56@i.ua', '+38 (032) 232-70-00', 'узвіз Чернігівський, буд. 79 кв. 08, Красноград, 93620');
INSERT INTO public.students VALUES (3, 'Наталія', 'Палій', 'panasudovychenko@i.ua', '015 728 50 58', 'площа Онезька, буд. 8 кв. 05, Носівка, 10362');
INSERT INTO public.students VALUES (4, 'Пилип', 'Кабалюк', 'emakarenko@ukr.net', '139-72-90', 'набережна Академіка Сахарова, буд. 63, Олександрія, 44779');
INSERT INTO public.students VALUES (5, 'Левко', 'Бандера', 'klyment40@gmail.com', '085 925-73-59', 'сквер Соборна, буд. 72, Гірник , 84051');
INSERT INTO public.students VALUES (6, 'Онисим', 'Даньків', 'poltavetsarkadii@meta.ua', '033 626-21-87', 'набережна Віри Холодної, буд. 58, Гнівань, 16495');
INSERT INTO public.students VALUES (7, 'Тимофій', 'Черненко', 'zlatoslavazinchenko@meta.ua', '+38 031 450 07 04', 'набережна Рівності, буд. 4, Запоріжжя, 52163');
INSERT INTO public.students VALUES (8, 'Гліб', 'Фартушняк', 'nataliia72@email.ua', '+38 037 270-34-91', 'вулиця Молодіжна, буд. 1, Зоринськ, 99411');
INSERT INTO public.students VALUES (9, 'Альберт', 'Тесленко', 'mhaievskyi@ukr.net', '027 06 82', 'сквер Рожева, буд. 0, Макіївка, 88391');
INSERT INTO public.students VALUES (10, 'Семен', 'Алексеєнко', 'chuikoarsen@i.ua', '091 662-98-20', 'сквер Заводська 4-та, буд. 2 кв. 96, Середина-Буда, 60825');


--
-- TOC entry 3346 (class 0 OID 16399)
-- Dependencies: 213
-- Data for Name: teachers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.teachers VALUES (1, 'Аніта', 'Андрійчук', 'obatih@i.ua', '+38 019 857-96-70', 'провулок Кустанайський 2-й, буд. 0, Лиман , 69602', '2022-02-18', '2023-01-11 19:14:00.537792');
INSERT INTO public.teachers VALUES (2, 'Данило', 'Юхименко', 'valentyn35@meta.ua', '+38 071 530 69 90', 'провулок Воронцовський, буд. 477 кв. 21, Шостка, 21386', '2022-04-24', '2023-01-11 19:14:00.537792');
INSERT INTO public.teachers VALUES (3, 'Євген', 'Шутько', 'atamaniukiaryna@meta.ua', '067 128-38-08', 'провулок Чорноморський 5-й, буд. 68 кв. 569, Гола Пристань, 95279', '2021-09-26', '2023-01-11 19:14:00.537792');
INSERT INTO public.teachers VALUES (4, 'Богуслава', 'Адамчук', 'sderehus@ukr.net', '+38 053 668-07-59', 'площа ім. К.Г. Паустовського, буд. 3 кв. 31, Городок, 56914', '2021-05-12', '2023-01-11 19:14:00.537792');
INSERT INTO public.teachers VALUES (5, 'Ілля', 'Теліженко', 'hryhorii89@gov.ua', '766-92-44', 'шосе Поїзна, буд. 109 кв. 395, Коростень, 66352', '2021-06-28', '2023-01-11 19:14:00.537792');


--
-- TOC entry 3348 (class 0 OID 16408)
-- Dependencies: 215
-- Data for Name: teachers_to_students; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.teachers_to_students VALUES (1, 4, 1);
INSERT INTO public.teachers_to_students VALUES (2, 2, 2);
INSERT INTO public.teachers_to_students VALUES (3, 1, 3);
INSERT INTO public.teachers_to_students VALUES (4, 1, 4);
INSERT INTO public.teachers_to_students VALUES (5, 2, 5);
INSERT INTO public.teachers_to_students VALUES (6, 2, 6);
INSERT INTO public.teachers_to_students VALUES (7, 1, 7);
INSERT INTO public.teachers_to_students VALUES (8, 1, 8);
INSERT INTO public.teachers_to_students VALUES (9, 3, 9);
INSERT INTO public.teachers_to_students VALUES (10, 1, 10);


--
-- TOC entry 3361 (class 0 OID 0)
-- Dependencies: 216
-- Name: contact_persons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_persons_id_seq', 15, true);


--
-- TOC entry 3362 (class 0 OID 0)
-- Dependencies: 210
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.students_id_seq', 10, true);


--
-- TOC entry 3363 (class 0 OID 0)
-- Dependencies: 212
-- Name: teachers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.teachers_id_seq', 5, true);


--
-- TOC entry 3364 (class 0 OID 0)
-- Dependencies: 214
-- Name: teachers_to_students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.teachers_to_students_id_seq', 10, true);


--
-- TOC entry 3191 (class 2606 OID 16388)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3199 (class 2606 OID 16432)
-- Name: contact_persons contact_persons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_persons
    ADD CONSTRAINT contact_persons_pkey PRIMARY KEY (id);


--
-- TOC entry 3193 (class 2606 OID 16397)
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- TOC entry 3195 (class 2606 OID 16406)
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (id);


--
-- TOC entry 3197 (class 2606 OID 16413)
-- Name: teachers_to_students teachers_to_students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers_to_students
    ADD CONSTRAINT teachers_to_students_pkey PRIMARY KEY (id);


--
-- TOC entry 3202 (class 2606 OID 16433)
-- Name: contact_persons contact_persons_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_persons
    ADD CONSTRAINT contact_persons_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.students(id) ON DELETE CASCADE;


--
-- TOC entry 3200 (class 2606 OID 16414)
-- Name: teachers_to_students teachers_to_students_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers_to_students
    ADD CONSTRAINT teachers_to_students_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.students(id) ON DELETE CASCADE;


--
-- TOC entry 3201 (class 2606 OID 16419)
-- Name: teachers_to_students teachers_to_students_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers_to_students
    ADD CONSTRAINT teachers_to_students_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES public.teachers(id) ON DELETE CASCADE;


-- Completed on 2023-02-17 19:37:23

--
-- PostgreSQL database dump complete
--

