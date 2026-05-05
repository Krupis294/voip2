-- PJSIP endpoints init script
-- Generated from pjsip.conf

BEGIN;

INSERT INTO ps_aors (id, max_contacts, qualify_frequency) VALUES
    ('10', 3, 60),
    ('11', 3, 60);

INSERT INTO ps_auths (id, auth_type, username, password) VALUES
    ('10', 'userpass', '10', '10'),
    ('11', 'userpass', '11', '11');

INSERT INTO ps_endpoints (id, transport, aors, auth, context, disallow, allow, direct_media) VALUES
    ('10', 'transport-udp-nat', '10', '10', 'from-internal', 'all', 'alaw', 'no'),
    ('11', 'transport-udp-nat', '11', '11', 'from-internal', 'all', 'alaw', 'no');

INSERT INTO ps_auths (id, auth_type, username, password) VALUES
    ('u54', 'userpass', 'u54', 'u54');

INSERT INTO ps_aors (id, max_contacts, qualify_frequency, contact) VALUES
    ('u41', 1, 60, 'sip:10.100.0.41'),
    ('u42', 1, 60, 'sip:10.100.0.42'),
    ('u43', 1, 60, NULL),
    ('u44', 1, 60, 'sip:10.100.0.44'),
    ('u45', 1, 60, 'sip:10.100.0.45'),
    ('u46', 1, 60, 'sip:10.100.0.46'),
    ('u47', 1, 60, 'sip:10.100.0.47'),
    ('u48', 1, 60, 'sip:10.100.0.48'),
    ('u49', 1, 60, 'sip:10.100.0.49'),
    ('u50', 1, 60, 'sip:10.100.0.50');

INSERT INTO ps_auths (id, auth_type, username, password) VALUES
    ('u41', 'userpass', 'u41', 'u41'),
    ('u42', 'userpass', 'u42', 'u42'),
    ('u43', 'userpass', 'u43', 'u43'),
    ('u44', 'userpass', 'u44', 'u44'),
    ('u45', 'userpass', 'u45', 'u45'),
    ('u46', 'userpass', 'u46', 'u46'),
    ('u47', 'userpass', 'u47', 'u47'),
    ('u48', 'userpass', 'u48', 'u48'),
    ('u49', 'userpass', 'u49', 'u49'),
    ('u50', 'userpass', 'u50', 'u50');

INSERT INTO ps_endpoints (id, transport, aors, auth, outbound_auth, context, disallow, allow, direct_media) VALUES
    ('u41', 'transport-udp-nat', 'u41', 'u41', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u42', 'transport-udp-nat', 'u42', 'u42', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u43', 'transport-udp-nat', 'u43', 'u43', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u44', 'transport-udp-nat', 'u44', 'u44', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u45', 'transport-udp-nat', 'u45', 'u45', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u46', 'transport-udp-nat', 'u46', 'u46', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u47', 'transport-udp-nat', 'u47', 'u47', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u48', 'transport-udp-nat', 'u48', 'u48', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u49', 'transport-udp-nat', 'u49', 'u49', 'u54', 'from-trunk', 'all', 'alaw', 'no'),
    ('u50', 'transport-udp-nat', 'u50', 'u50', 'u54', 'from-trunk', 'all', 'alaw', 'no');

COMMIT;
