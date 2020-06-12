function att = attenuationWetAir(f, t, p, ro)
    % approximation valid up to 350 GHz
    e = ro * (t + 273.15) / 216.7;
    ptot = p + e;

    rp = ptot / 1013;
    rt = 288 / (273 + t);
    
    eta1 = 0.955 * rp * rt^(0.68) + 0.006 * ro;
    eta2 = 0.735 * rp * rt^(0.5) + 0.0353 * rt^4 * ro;
    
    gamma1 = g(f, 22) .* (3.98 * eta1 * exp(2.23 * (1 - rt))) ./ ((f - 22.235).^2 + 9.42 * eta1^2) ...
        + (11.96 * eta1 * exp(0.7 * (1 - rt))) ./ ((f - 183.31).^2 + 11.14 * eta1^2);
    gamma2 = ((0.081 * eta1 * exp(6.44 * (1 - rt))) ./ ((f - 321.226).^2 + 6.29 * eta1^2)) ...
        + ((3.66 * eta1 * exp(1.6 * (1 - rt))) ./ ((f - 325.153).^2 + 9.22 * eta1^2));
    gamma3 = ((25.37 * eta1 * exp(1.09 * (1 - rt))) ./ ((f - 380).^2)) ...
        + ((17.4 * eta1 * exp(1.46 * (1 - rt))) ./((f - 448).^2));
    gamma4 = (g(f, 557) .* (844.6 * eta1 * exp(0.17 * (1 - rt))) ./((f - 557).^2)) ...
        + (g(f, 752) .* (290 * eta1 * exp(0.41 * (1 - rt))) ./((f - 752).^2));
    gamma5 = g(f, 1780) .* (8.3328e4 * eta2 * exp(0.99 * (1 - rt))) ./((f - 1780).^2);
    gammaw = (gamma1 + gamma2 + gamma3 + gamma4 + gamma5) .* f.^2 * rt^(2.5) * ro * 1e-4;
    
    sigmaw = 1.013 ./ (1 + exp(-8.6 * (rp - 0.57)));

    t1 = (1.39 * sigmaw) ./ ((f - 22.235).^2 + 2.56 * sigmaw);
    t2 = (3.37 * sigmaw) ./ ((f - 183.31).^2 + 4.69 * sigmaw);
    t3 = (1.58 * sigmaw) ./ ((f - 325.1).^2 + 2.89 * sigmaw);

    hw = 1.66 * (1 + t1 + t2 + t3);

    att = gammaw .* hw;
end
