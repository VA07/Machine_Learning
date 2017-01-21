#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    out_perc = 10 #perecntage of outliers
	
	#convert to lists for ease of operation
    age = ages.tolist()
    pred = predictions.tolist()
    net_worth = net_worths.tolist()	
	
	#Calculate the residual errors
    res_error = []
    for i in xrange(len(predictions)):
        res_error.append(net_worths[i] - predictions[i])

    for i in xrange(len(pred)*out_perc/100):
        ind = res_error.index(min(res_error))
        print ind , res_error[ind]
        del res_error[ind]
        del age[ind]
        del net_worth[ind]	 
  
    
    for i in xrange(len(age) ):
	    cleaned_data.append(([age[i]],[net_worth[i]], [res_error[i]]))

    return cleaned_data


