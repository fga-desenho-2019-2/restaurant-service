--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0 (Debian 12.0-2.pgdg100+1)
-- Dumped by pg_dump version 12.0 (Debian 12.0-2.pgdg100+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO admin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: corsheaders_corsmodel; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.corsheaders_corsmodel (
    id integer NOT NULL,
    cors character varying(255) NOT NULL
);


ALTER TABLE public.corsheaders_corsmodel OWNER TO admin;

--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.corsheaders_corsmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.corsheaders_corsmodel_id_seq OWNER TO admin;

--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.corsheaders_corsmodel_id_seq OWNED BY public.corsheaders_corsmodel.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Name: restaurant_service_complement; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_complement (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description character varying(200) NOT NULL,
    value double precision NOT NULL,
    selected boolean NOT NULL,
    qtd integer NOT NULL,
    item_id integer NOT NULL
);


ALTER TABLE public.restaurant_service_complement OWNER TO admin;

--
-- Name: restaurant_service_complement_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.restaurant_service_complement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_service_complement_id_seq OWNER TO admin;

--
-- Name: restaurant_service_complement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.restaurant_service_complement_id_seq OWNED BY public.restaurant_service_complement.id;


--
-- Name: restaurant_service_imageitem; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_imageitem (
    id integer NOT NULL,
    image character varying(255) NOT NULL,
    item_id integer NOT NULL
);


ALTER TABLE public.restaurant_service_imageitem OWNER TO admin;

--
-- Name: restaurant_service_imageitem_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.restaurant_service_imageitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_service_imageitem_id_seq OWNER TO admin;

--
-- Name: restaurant_service_imageitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.restaurant_service_imageitem_id_seq OWNED BY public.restaurant_service_imageitem.id;


--
-- Name: restaurant_service_imagerestaurant; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_imagerestaurant (
    id integer NOT NULL,
    image character varying(255) NOT NULL,
    restaurant_id character varying(16) NOT NULL
);


ALTER TABLE public.restaurant_service_imagerestaurant OWNER TO admin;

--
-- Name: restaurant_service_imagerestaurant_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.restaurant_service_imagerestaurant_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_service_imagerestaurant_id_seq OWNER TO admin;

--
-- Name: restaurant_service_imagerestaurant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.restaurant_service_imagerestaurant_id_seq OWNED BY public.restaurant_service_imagerestaurant.id;


--
-- Name: restaurant_service_item; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_item (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    value double precision NOT NULL,
    details text NOT NULL,
    category character varying(50) NOT NULL,
    restaurant_cnpj character varying(16) NOT NULL
);


ALTER TABLE public.restaurant_service_item OWNER TO admin;

--
-- Name: restaurant_service_item_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.restaurant_service_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_service_item_id_seq OWNER TO admin;

--
-- Name: restaurant_service_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.restaurant_service_item_id_seq OWNED BY public.restaurant_service_item.id;


--
-- Name: restaurant_service_itemcategory; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_itemcategory (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.restaurant_service_itemcategory OWNER TO admin;

--
-- Name: restaurant_service_itemcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.restaurant_service_itemcategory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_service_itemcategory_id_seq OWNER TO admin;

--
-- Name: restaurant_service_itemcategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.restaurant_service_itemcategory_id_seq OWNED BY public.restaurant_service_itemcategory.id;


--
-- Name: restaurant_service_menu; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_menu (
    id integer NOT NULL,
    description character varying(200) NOT NULL,
    restaurant_id character varying(16) NOT NULL
);


ALTER TABLE public.restaurant_service_menu OWNER TO admin;

--
-- Name: restaurant_service_menu_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.restaurant_service_menu_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_service_menu_id_seq OWNER TO admin;

--
-- Name: restaurant_service_menu_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.restaurant_service_menu_id_seq OWNED BY public.restaurant_service_menu.id;


--
-- Name: restaurant_service_restaurant; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_restaurant (
    cnpj character varying(16) NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(200) NOT NULL,
    note double precision NOT NULL,
    wait_time interval NOT NULL,
    category_id integer NOT NULL,
    shopping_id character varying(16) NOT NULL
);


ALTER TABLE public.restaurant_service_restaurant OWNER TO admin;

--
-- Name: restaurant_service_restaurantcategory; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_restaurantcategory (
    id integer NOT NULL,
    name character varying(60) NOT NULL
);


ALTER TABLE public.restaurant_service_restaurantcategory OWNER TO admin;

--
-- Name: restaurant_service_restaurantcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.restaurant_service_restaurantcategory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_service_restaurantcategory_id_seq OWNER TO admin;

--
-- Name: restaurant_service_restaurantcategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.restaurant_service_restaurantcategory_id_seq OWNED BY public.restaurant_service_restaurantcategory.id;


--
-- Name: restaurant_service_shopping; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.restaurant_service_shopping (
    created timestamp with time zone NOT NULL,
    cnpj character varying(16) NOT NULL,
    name character varying(100) NOT NULL,
    city character varying(100) NOT NULL,
    state character varying(30) NOT NULL,
    country character varying(50) NOT NULL,
    neighborhood character varying(50) NOT NULL,
    cep character varying(8) NOT NULL,
    number integer NOT NULL,
    phone character varying(12) NOT NULL
);


ALTER TABLE public.restaurant_service_shopping OWNER TO admin;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: corsheaders_corsmodel id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.corsheaders_corsmodel ALTER COLUMN id SET DEFAULT nextval('public.corsheaders_corsmodel_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: restaurant_service_complement id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_complement ALTER COLUMN id SET DEFAULT nextval('public.restaurant_service_complement_id_seq'::regclass);


--
-- Name: restaurant_service_imageitem id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_imageitem ALTER COLUMN id SET DEFAULT nextval('public.restaurant_service_imageitem_id_seq'::regclass);


--
-- Name: restaurant_service_imagerestaurant id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_imagerestaurant ALTER COLUMN id SET DEFAULT nextval('public.restaurant_service_imagerestaurant_id_seq'::regclass);


--
-- Name: restaurant_service_item id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_item ALTER COLUMN id SET DEFAULT nextval('public.restaurant_service_item_id_seq'::regclass);


--
-- Name: restaurant_service_itemcategory id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_itemcategory ALTER COLUMN id SET DEFAULT nextval('public.restaurant_service_itemcategory_id_seq'::regclass);


--
-- Name: restaurant_service_menu id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_menu ALTER COLUMN id SET DEFAULT nextval('public.restaurant_service_menu_id_seq'::regclass);


--
-- Name: restaurant_service_restaurantcategory id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_restaurantcategory ALTER COLUMN id SET DEFAULT nextval('public.restaurant_service_restaurantcategory_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add cors model	1	add_corsmodel
2	Can change cors model	1	change_corsmodel
3	Can delete cors model	1	delete_corsmodel
4	Can view cors model	1	view_corsmodel
5	Can add log entry	2	add_logentry
6	Can change log entry	2	change_logentry
7	Can delete log entry	2	delete_logentry
8	Can view log entry	2	view_logentry
9	Can add permission	3	add_permission
10	Can change permission	3	change_permission
11	Can delete permission	3	delete_permission
12	Can view permission	3	view_permission
13	Can add group	4	add_group
14	Can change group	4	change_group
15	Can delete group	4	delete_group
16	Can view group	4	view_group
17	Can add user	5	add_user
18	Can change user	5	change_user
19	Can delete user	5	delete_user
20	Can view user	5	view_user
21	Can add content type	6	add_contenttype
22	Can change content type	6	change_contenttype
23	Can delete content type	6	delete_contenttype
24	Can view content type	6	view_contenttype
25	Can add session	7	add_session
26	Can change session	7	change_session
27	Can delete session	7	delete_session
28	Can view session	7	view_session
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: corsheaders_corsmodel; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.corsheaders_corsmodel (id, cors) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	corsheaders	corsmodel
2	admin	logentry
3	auth	permission
4	auth	group
5	auth	user
6	contenttypes	contenttype
7	sessions	session
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-11-17 22:53:52.783928+00
2	auth	0001_initial	2019-11-17 22:53:52.834593+00
3	admin	0001_initial	2019-11-17 22:53:52.907181+00
4	admin	0002_logentry_remove_auto_add	2019-11-17 22:53:52.934941+00
5	admin	0003_logentry_add_action_flag_choices	2019-11-17 22:53:52.946943+00
6	contenttypes	0002_remove_content_type_name	2019-11-17 22:53:52.981507+00
7	auth	0002_alter_permission_name_max_length	2019-11-17 22:53:52.988546+00
8	auth	0003_alter_user_email_max_length	2019-11-17 22:53:53.000552+00
9	auth	0004_alter_user_username_opts	2019-11-17 22:53:53.016648+00
10	auth	0005_alter_user_last_login_null	2019-11-17 22:53:53.028136+00
11	auth	0006_require_contenttypes_0002	2019-11-17 22:53:53.031214+00
12	auth	0007_alter_validators_add_error_messages	2019-11-17 22:53:53.050096+00
13	auth	0008_alter_user_username_max_length	2019-11-17 22:53:53.066242+00
14	auth	0009_alter_user_last_name_max_length	2019-11-17 22:53:53.07919+00
15	auth	0010_alter_group_name_max_length	2019-11-17 22:53:53.091154+00
16	auth	0011_update_proxy_permissions	2019-11-17 22:53:53.106796+00
17	corsheaders	0001_initial	2019-11-17 22:53:53.115203+00
18	restaurant_service	0001_initial	2019-11-17 22:53:53.203392+00
19	sessions	0001_initial	2019-11-17 22:53:53.254413+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: restaurant_service_complement; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_complement (id, name, description, value, selected, qtd, item_id) FROM stdin;
1	Suco Natural	Jarra de suco da Fruta	7.99	f	1	1
2	Laranja	Fruta	1.99	f	1	2
3	Suco Natural	Jarra de suco da Fruta	7.99	f	1	2
4	Queijão	Queijo ralado	2.5	f	1	3
5	Borda	Borda de catupiry	5	f	1	4
6	Ovo marinado	Ovo marinado	1	f	2	5
7	Molho extra	Molho a bolonhesa extra	2	f	1	6
\.


--
-- Data for Name: restaurant_service_imageitem; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_imageitem (id, image, item_id) FROM stdin;
1	item_images/01a8bf08-8dc4-4539-b20d-616d6ba5a907.jpg	1
2	item_images/0803c46b-9069-4b51-b8e5-622289f9f4b8.jpg	2
3	item_images/02c31d98-f965-494a-8a6a-9498c4374e98.jpg	3
4	item_images/1cb4ce12-4424-43ac-9ed9-deafdb3c78ce.jpg	4
5	item_images/019928ed-b146-4e06-b17c-c5da08ac5245.jpg	5
6	item_images/44681eec-8ada-4677-b4cf-11b9336a916b.jpg	6
\.


--
-- Data for Name: restaurant_service_imagerestaurant; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_imagerestaurant (id, image, restaurant_id) FROM stdin;
1	restaurant_images/339dbd21-ee8e-42dc-8221-3f2182e9d98c.jpg	567843321745
2	restaurant_images/55cab2c9-2add-43ee-8e05-0c197d702efa.jpg	05712768000101
\.


--
-- Data for Name: restaurant_service_item; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_item (id, name, value, details, category, restaurant_cnpj) FROM stdin;
1	Especial do Chef	18.5	Prato especial do chef.	1	567843321745
2	Feijoada	22	Feijoada tradicional.	1	567843321745
3	Macarrão	25	Macarrão ao alho e óleo e temperos diversos.	1	567843321745
4	Pizza de banana	30	Pizza de banana com queijo mussarela.	2	05712768000101
5	Shoyu Tyashu Lamen	27	Lamen tradicional , com caldo encorpado à base de shoyu.	2	05712768000101
6	Lasanha vegetariana	22.19	Lasanha de legumes, queijo mussarela e massa tradicional.	2	05712768000101
\.


--
-- Data for Name: restaurant_service_itemcategory; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_itemcategory (id, name) FROM stdin;
1	Prato Principal
2	Massas
\.


--
-- Data for Name: restaurant_service_menu; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_menu (id, description, restaurant_id) FROM stdin;
\.


--
-- Data for Name: restaurant_service_restaurant; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_restaurant (cnpj, name, description, note, wait_time, category_id, shopping_id) FROM stdin;
567843321745	Pé de Fava		4	00:30:00	1	1
05712768000101	Saborear		4.6	00:15:00	1	1
\.


--
-- Data for Name: restaurant_service_restaurantcategory; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_restaurantcategory (id, name) FROM stdin;
1	Comida Brasileira
\.


--
-- Data for Name: restaurant_service_shopping; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.restaurant_service_shopping (created, cnpj, name, city, state, country, neighborhood, cep, number, phone) FROM stdin;
2019-11-17 22:54:00.608625+00	1	Shopping Sul	Gama	DF	Brasil		123456	40	213213
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 28, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.corsheaders_corsmodel_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 7, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 19, true);


--
-- Name: restaurant_service_complement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.restaurant_service_complement_id_seq', 7, true);


--
-- Name: restaurant_service_imageitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.restaurant_service_imageitem_id_seq', 6, true);


--
-- Name: restaurant_service_imagerestaurant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.restaurant_service_imagerestaurant_id_seq', 2, true);


--
-- Name: restaurant_service_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.restaurant_service_item_id_seq', 6, true);


--
-- Name: restaurant_service_itemcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.restaurant_service_itemcategory_id_seq', 2, true);


--
-- Name: restaurant_service_menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.restaurant_service_menu_id_seq', 1, false);


--
-- Name: restaurant_service_restaurantcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.restaurant_service_restaurantcategory_id_seq', 1, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: corsheaders_corsmodel corsheaders_corsmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.corsheaders_corsmodel
    ADD CONSTRAINT corsheaders_corsmodel_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: restaurant_service_complement restaurant_service_complement_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_complement
    ADD CONSTRAINT restaurant_service_complement_pkey PRIMARY KEY (id);


--
-- Name: restaurant_service_imageitem restaurant_service_imageitem_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_imageitem
    ADD CONSTRAINT restaurant_service_imageitem_pkey PRIMARY KEY (id);


--
-- Name: restaurant_service_imagerestaurant restaurant_service_imagerestaurant_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_imagerestaurant
    ADD CONSTRAINT restaurant_service_imagerestaurant_pkey PRIMARY KEY (id);


--
-- Name: restaurant_service_item restaurant_service_item_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_item
    ADD CONSTRAINT restaurant_service_item_pkey PRIMARY KEY (id);


--
-- Name: restaurant_service_itemcategory restaurant_service_itemcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_itemcategory
    ADD CONSTRAINT restaurant_service_itemcategory_pkey PRIMARY KEY (id);


--
-- Name: restaurant_service_menu restaurant_service_menu_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_menu
    ADD CONSTRAINT restaurant_service_menu_pkey PRIMARY KEY (id);


--
-- Name: restaurant_service_restaurant restaurant_service_restaurant_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_restaurant
    ADD CONSTRAINT restaurant_service_restaurant_pkey PRIMARY KEY (cnpj);


--
-- Name: restaurant_service_restaurantcategory restaurant_service_restaurantcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_restaurantcategory
    ADD CONSTRAINT restaurant_service_restaurantcategory_pkey PRIMARY KEY (id);


--
-- Name: restaurant_service_shopping restaurant_service_shopping_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_shopping
    ADD CONSTRAINT restaurant_service_shopping_pkey PRIMARY KEY (cnpj);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: restaurant_service_complement_item_id_2ea22079; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_complement_item_id_2ea22079 ON public.restaurant_service_complement USING btree (item_id);


--
-- Name: restaurant_service_imageitem_item_id_2db28e79; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_imageitem_item_id_2db28e79 ON public.restaurant_service_imageitem USING btree (item_id);


--
-- Name: restaurant_service_imagerestaurant_restaurant_id_e68c0f02; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_imagerestaurant_restaurant_id_e68c0f02 ON public.restaurant_service_imagerestaurant USING btree (restaurant_id);


--
-- Name: restaurant_service_imagerestaurant_restaurant_id_e68c0f02_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_imagerestaurant_restaurant_id_e68c0f02_like ON public.restaurant_service_imagerestaurant USING btree (restaurant_id varchar_pattern_ops);


--
-- Name: restaurant_service_menu_restaurant_id_f3df913a; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_menu_restaurant_id_f3df913a ON public.restaurant_service_menu USING btree (restaurant_id);


--
-- Name: restaurant_service_menu_restaurant_id_f3df913a_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_menu_restaurant_id_f3df913a_like ON public.restaurant_service_menu USING btree (restaurant_id varchar_pattern_ops);


--
-- Name: restaurant_service_restaurant_category_id_d239a6b4; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_restaurant_category_id_d239a6b4 ON public.restaurant_service_restaurant USING btree (category_id);


--
-- Name: restaurant_service_restaurant_cnpj_4e103578_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_restaurant_cnpj_4e103578_like ON public.restaurant_service_restaurant USING btree (cnpj varchar_pattern_ops);


--
-- Name: restaurant_service_restaurant_shopping_id_ca9b0943; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_restaurant_shopping_id_ca9b0943 ON public.restaurant_service_restaurant USING btree (shopping_id);


--
-- Name: restaurant_service_restaurant_shopping_id_ca9b0943_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_restaurant_shopping_id_ca9b0943_like ON public.restaurant_service_restaurant USING btree (shopping_id varchar_pattern_ops);


--
-- Name: restaurant_service_shopping_cnpj_018689d2_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX restaurant_service_shopping_cnpj_018689d2_like ON public.restaurant_service_shopping USING btree (cnpj varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: restaurant_service_complement restaurant_service_c_item_id_2ea22079_fk_restauran; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_complement
    ADD CONSTRAINT restaurant_service_c_item_id_2ea22079_fk_restauran FOREIGN KEY (item_id) REFERENCES public.restaurant_service_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: restaurant_service_imageitem restaurant_service_i_item_id_2db28e79_fk_restauran; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_imageitem
    ADD CONSTRAINT restaurant_service_i_item_id_2db28e79_fk_restauran FOREIGN KEY (item_id) REFERENCES public.restaurant_service_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: restaurant_service_imagerestaurant restaurant_service_i_restaurant_id_e68c0f02_fk_restauran; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_imagerestaurant
    ADD CONSTRAINT restaurant_service_i_restaurant_id_e68c0f02_fk_restauran FOREIGN KEY (restaurant_id) REFERENCES public.restaurant_service_restaurant(cnpj) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: restaurant_service_menu restaurant_service_m_restaurant_id_f3df913a_fk_restauran; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_menu
    ADD CONSTRAINT restaurant_service_m_restaurant_id_f3df913a_fk_restauran FOREIGN KEY (restaurant_id) REFERENCES public.restaurant_service_restaurant(cnpj) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: restaurant_service_restaurant restaurant_service_r_category_id_d239a6b4_fk_restauran; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_restaurant
    ADD CONSTRAINT restaurant_service_r_category_id_d239a6b4_fk_restauran FOREIGN KEY (category_id) REFERENCES public.restaurant_service_restaurantcategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: restaurant_service_restaurant restaurant_service_r_shopping_id_ca9b0943_fk_restauran; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.restaurant_service_restaurant
    ADD CONSTRAINT restaurant_service_r_shopping_id_ca9b0943_fk_restauran FOREIGN KEY (shopping_id) REFERENCES public.restaurant_service_shopping(cnpj) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

