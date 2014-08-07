#  Copyright CERFACS (http://cerfacs.fr/)
#  Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
#
#  Author: Natalia Tatarinova <tatarinova@cerfacs.fr>


# set the attributs "long_name" and "units" of indice variable in output meta data
# (for indices with user defined thrshold)


def SU_setthresholdattr(threshold_var):
    threshold_var.setncattr('long_name', "Threshold temperature in degrees Celsius")
    threshold_var.setncattr('standard_name', "air_temperature")
    threshold_var.setncattr('units', "degrees Celsius")

def SU_setvarattr(var_nc, threshold):
    long_name_str = 'Number of days with daily maximum temperature > {0} degrees)'.format(threshold)
    var_nc.setncattr('long_name', long_name_str)
    var_nc.setncattr('units', 'days')

def CSU_setthresholdattr(threshold_var):
    threshold_var.setncattr('long_name', "Threshold temperature in degrees Celsius")
    threshold_var.setncattr('standard_name', "air_temperature")
    threshold_var.setncattr('units', "degrees Celsius")
    
def CSU_setvarattr(var_nc, threshold):
    long_name_str = 'Maximum number of consecutive days with daily maximum temperature > {0} degrees)'.format(threshold)
    var_nc.setncattr('long_name', long_name_str)
    var_nc.setncattr('units', 'days')

def TR_setthresholdattr(threshold_var):
    threshold_var.setncattr('long_name', "Threshold temperature in degrees Celsius")
    threshold_var.setncattr('standard_name', "air_temperature")
    threshold_var.setncattr('units', "degrees Celsius")
    
def TR_setvarattr(var_nc, threshold):
    long_name_str = 'Number of days with daily minimum temperature > {0} degrees'.format(threshold)
    var_nc.setncattr('long_name', long_name_str)
    var_nc.setncattr('units', 'days')

