INSERT INTO public.email (address, uuid, verified, verification_string) VALUES ('test@gmail.com', 'c76df330-2c15-4487-8e97-a217a7385ef9', true, 'a8ff065016eb55fc2f290b3994338fe8e2a9d55c4ae3159f2ec124ffac051b8c');
INSERT INTO public.subscription (id, email, district) VALUES ('4f72a371-460c-5468-ba71-27e396d57bb7', 'test@gmail.com', 'Davis District');
INSERT INTO public."user" (username, full_name, email, password, enabled) VALUES ('test', 'test', 'test@gmail.com', '$2b$12$kL0FmkBAb.tCeklnYOLESu1Rv56WntP9cagJo/ODUHAxrfWTLYXa2', true);
